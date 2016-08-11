import datetime
from django.db.models import Manager
from django.utils import six
from django.conf import settings
from django.utils.timezone import utc
from mongoengine.errors import DoesNotExist
from rest_framework import status


class GenericRESTAPITestCaseMixin(object):

    def get_create_response(self, data=None, **kwargs):
        return super(GenericRESTAPITestCaseMixin, self).get_create_response(data, **{'format': 'json'})

    def get_update_response(self, data=None, results=None, use_patch=None, **kwargs):
        return super(GenericRESTAPITestCaseMixin, self).get_update_response(data, results, use_patch, **{'format': 'json'})

    def _update_check_db(self, obj, data=None, results=None):
        if data is None:
            data = self.get_update_data()

        if results is None:
            results = self.get_update_results(data) or {}

        for key, value in six.iteritems(data):
            # check if ``obj`` is a dict to allow overriding ``_update_check_db()``
            # and perform checks on a serialized object
            if isinstance(obj, dict):
                attribute = obj.get(key)
                if isinstance(attribute, list):
                    self.assertListEqual(attribute, value)
                    continue
            else:
                # check for foreign key
                if hasattr(obj, '%s_id' % key):
                    related = getattr(obj, key)
                    attribute = self.get_relationship_value(related, key)
                elif hasattr(obj, key):
                    attribute = getattr(obj, key)

                    if hasattr(self, 'validate_update_%s' % key):
                        validation = getattr(self, 'validate_update_%s' % key)
                        validation(obj, results.get(key, value))
                        continue

                    # Handle case of a ManyToMany relation
                    elif isinstance(attribute, Manager):
                        items = {self.get_relationship_value(item, key) for item in attribute.all()}
                        self.assertTrue(set(value).issubset(items))
                        continue

                    elif isinstance(attribute, dict):
                        results[key] = {settings.DEFAULT_CONTENT_LANGUAGE_CODE: results.get(key, value)}

                    elif isinstance(attribute, datetime.datetime):
                        results[key] = datetime.datetime.utcfromtimestamp(int(results.get(key, value))).replace(tzinfo=utc)

                else:
                    custom_validate = getattr(self, 'validate_update_%s' % key, None)
                    self.assertTrue(custom_validate, 'Not found model attribute "%s" - add custom validation "validate_update_%s"' % (key, key))

                    custom_validate(obj, results.get(key, value))
                    continue

            self.assertEqual(attribute, results.get(key, value))


class MongoDestroyRESTAPITestCaseMixin(object):

    def test_destroy(self, **kwargs):
        """Send request to the destroy view endpoint, verify and return the response.

                Also verifies the object does not exist anymore in the database.

                :param kwargs: Extra arguments that are passed to the client's ``delete()`` call.
                :returns: The view's response.
                """

        response = self.get_destroy_response(**kwargs)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)
        # Another sanity check:
        # see that the instance is removed from the database.
        self.assertRaises(DoesNotExist, self.object.__class__.objects.get, **{self.lookup_field: self.object_id})

        return response
