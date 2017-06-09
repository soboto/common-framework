import factory
import uuid
from sbt_common import models
from sbt_common import constants


class AuthUserFactory(factory.Factory):
    class Meta:
        model = models.AuthUser
        abstract = True

    id = uuid.uuid4()
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)
    username = factory.Sequence(lambda n: 'john%s' % n)
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    is_active = True


class BOUserFactory(AuthUserFactory):
    class Meta:
        model = models.BOUser
        abstract = False

    type = constants.BO_USER_TYPE
    is_superuser = True  # TODO: change this and add permissions


class CustomerUserFactory(AuthUserFactory):
    class Meta:
        model = models.Customer
        abstract = False

    type = constants.CUSTOMER_USER_TYPE


class AnonymousUserFactory(AuthUserFactory):
    class Meta:
        model = models.Anonymous
        abstract = False

    type = constants.ANONYMOUS_USER_TYPE
