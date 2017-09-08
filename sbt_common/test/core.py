from rest_framework.reverse import reverse
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.utils import six
import factory
from uuid import UUID
from django.utils.six import text_type
from rest_framework.test import APITestCase
from datetime import datetime

from sbt_common.test.authentication import fake_authentication
from sbt_common.utils import datetime_to_epoch


class CoreRESTAPITestCase(APITestCase):
    #: *required*: Base route name of the API endpoints to test.
    base_name = None
    #: *required*: The factory class to use for creating the main object to test against.
    factory_class = None
    #: Suffix for list endpoint view names. Defaults to ``'-list'``.
    LIST_SUFFIX = '-list'
    #: Suffix for detail endpoint view names. Defaults to ``'-detail'``.
    DETAIL_SUFFIX = '-detail'
    #: The user instance created if the ``user_factory`` is set and used. Defaults to ``None``.
    lookup_field = 'pk'
    user = None
    user_type = None

    def get_factory_class(self):
        """Return the factory class for generating the main object (or model instance) of this test case.

        By default this gets the ``factory_class`` attribute of this class.

        :returns: Factory class used for creating the mock objects.
        """

        return getattr(self, 'factory_class')

    def create_object(self):
        factory = self.get_factory_class()
        return factory.create()

    def setUp(self):
        self.user = fake_authentication.authenticate_user(self.user_type)

        if hasattr(self, 'entity_id'):
            fake_authentication.set_user_entity(self.entity_id)

    def tearDown(self):
        print 'tearDown'

    def get_url_args(self, object_id=None):
        if object_id is not None:
            return [object_id]

        return []

    def get_list_url(self):
        """Return the list endpoint url.

        :returns: The url of list endpoint.
        """

        return reverse(self.base_name + self.LIST_SUFFIX, args=self.get_url_args())

    def get_detail_url(self, object_id):
        """Return the detail endpoint url.

        :returns: The url of detail endpoint.
        """
        return reverse(self.base_name + self.DETAIL_SUFFIX, args=self.get_url_args(object_id))

    def get_create_url(self):
        """Return the create endpoint url.

        :returns: The url of create endpoint.
        """

        return reverse(self._get_create_name(), args=self.get_url_args())

    def get_destroy_url(self, object_id):
        """Return the destroy endpoint url.

        :returns: The url of destroy endpoint.
        """
        return reverse(self._get_destroy_name(), args=self.get_url_args(object_id))

    def get_update_url(self, object_id):
        """Return the update endpoint url.

        :returns: The url of update endpoint.
        """
        return reverse(self._get_update_name(), args=self.get_url_args(object_id))

    def _get_create_name(self):
        if hasattr(self, 'create_name'):
            view_name = self.create_name
        else:
            view_name = self.base_name + self.LIST_SUFFIX

        return view_name

    def _get_destroy_name(self):
        if hasattr(self, 'destroy_name'):
            view_name = self.destroy_name
        else:
            view_name = self.base_name + self.DETAIL_SUFFIX

        return view_name

    def _get_update_name(self):
        if hasattr(self, 'update_name'):
            view_name = self.update_name
        else:
            view_name = self.base_name + self.DETAIL_SUFFIX

        return view_name


class ListAPITestCaseMixin(object):
    pagination_results_field = None

    def get_list_response(self, **kwargs):
        return self.client.get(self.get_list_url(), **kwargs)

    def _list(self, **kwargs):
        self.create_object()

        response = self.get_list_response(**kwargs)
        results = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK, results)

        if self.pagination_results_field:
            self.assertIn(self.pagination_results_field, results)
            results = results[self.pagination_results_field]

        self.assertTrue(len(results) >= 1)

        return response


class CreateAPITestCaseMixin(object):
    pagination_results_field = None
    response_lookup_field = 'id'

    def get_create_data(self):
        return factory.build(dict, FACTORY_CLASS=self.factory_class)

    def get_create_response(self, data=None, **kwargs):

        if data is None:
            data = self.get_create_data()

        return self.client.post(self.get_create_url(), data or {}, **{'format': 'json'})

    def get_lookup_from_response(self, data):
        return data.get(self.response_lookup_field)

    def _create(self, **kwargs):
        response = self.get_create_response(**kwargs)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, getattr(response, 'data', response))

        # another sanity check:
        # getting the instance from database simply to see that it's found and does not raise any exception
        created = self.factory_class._meta.model.objects.get(
            **{self.lookup_field: self.get_lookup_from_response(response.data)})

        return response, created


class DestroyAPITestCaseMixin(object):

    def get_destroy_response(self, object_id, **kwargs):
        return self.client.delete(self.get_destroy_url(object_id), **kwargs)

    def _destroy(self, object_id=None, **kwargs):
        if object_id is None:
            obj = self.create_object()
            object_id = obj.id

        print 'AAAAA'
        print object_id
        
        response = self.get_destroy_response(object_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)
        # Another sanity check:
        # see that the instance is removed from the database.
        self.assertRaises(ObjectDoesNotExist,
                          self.factory_class._meta.model.objects.get, **{self.lookup_field: object_id})

        return response


class UpdateAPITestCaseMixin(object):
    use_patch = True
    update_data = None

    def get_update_data(self):
        return self.update_data

    def get_update_response(self, object_id, **kwargs):

        data = self.get_update_data()
        self.__data = data

        args = [self.get_update_url(object_id), data]
        kwargs = {'format': 'json'}

        return self.client.patch(*args, **kwargs) if self.use_patch else self.client.put(*args, **kwargs)

    def _update(self, object_id=None, **kwargs):
        if object_id is None:
            obj = self.create_object()
            object_id = obj.id

        response = self.get_update_response(object_id, **kwargs)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # getting a fresh copy of the object from DB
        updated = self.factory_class._meta.model.objects.get(**{self.lookup_field: object_id})
        # Sanity check:
        # check that the copy in the database was updated as expected.
        self._update_check_db(updated)

        return response, updated

    def _update_check_object(self, obj, data):
        for key, value in six.iteritems(data):
            attribute = getattr(obj, key)

            self._update_check_object_field(attribute, value, key)

    def _update_check_object_field(self, attribute, value, key):
        if isinstance(attribute, datetime):
            attribute = datetime_to_epoch(attribute)

        elif isinstance(attribute, UUID):
            attribute = str(attribute)

        elif isinstance(attribute, unicode):
            value = unicode(value)

        self.assertEqual(attribute, value, key)

    def _update_check_db(self, obj):
        data = self.__data

        for key, value in six.iteritems(data):
            attribute = getattr(obj, key)

            if hasattr(self, 'update_check_db_%s' % key):
                validation = getattr(self, 'update_check_db_%s' % key)
                validation(attribute, value)
                continue

            self._update_check_object_field(attribute, value, key)


class CRUDAPITestCaseMixin(CreateAPITestCaseMixin,
                           ListAPITestCaseMixin,
                           UpdateAPITestCaseMixin,
                           DestroyAPITestCaseMixin):
    pass
