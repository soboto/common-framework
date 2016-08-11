from django import test
from django.conf import settings
from mongoengine import connect
from mongoengine import connection
from mongoengine.connection import get_db, get_connection, disconnect
from mongoengine.errors import DoesNotExist
from rest_framework import status


class MongoTestCase(test.SimpleTestCase):
    """
    TestCase class that clear the collection between the tests
    """
    assertQuerysetEqual = test.TransactionTestCase.__dict__['assertQuerysetEqual']

    def _pre_setup(self):
        """ (MongoTestMixin) -> (NoneType)
        create a new mongo connection.
        """
        super(MongoTestCase, self)._pre_setup()

        for alias, conn_settings in settings.MONGODB_DATABASES.items():
            connection.register_connection(alias, **conn_settings)

        self.db = connect(get_db())

    def _post_teardown(self):
        connection = get_connection()
        connection.drop_database(get_db())
        disconnect()

        #super(MongoTestCase, self)._post_teardown()


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