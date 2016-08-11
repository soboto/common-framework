from django import test
from django.conf import settings
from mongoengine import connect
from mongoengine import connection
from mongoengine.connection import get_db, get_connection, disconnect


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