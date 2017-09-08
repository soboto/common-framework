# -*- coding: utf-8 -*-
from rest_framework.authentication import TokenAuthentication
from sbt_common.constants import SUPPLIER

from . import _factories


class FakeUserAuthentication(object):
    _authenticated_user = None
    _auth_users = {
        'bo-user': _factories.BOUserFactory,
        'customer': _factories.CustomerUserFactory,
        'anonymous': _factories.AnonymousUserFactory,
    }

    def authenticate_user(self, key):
        if key not in self._auth_users:
            raise Exception('User not found')

        self._authenticated_user = self._auth_users[key].create()

        return self.get_authenticated_user()

    def get_authenticated_user(self):
        return self._authenticated_user

    def set_user_entity(self, entity_id):
        self._authenticated_user.entity = entity_id
        self._authenticated_user.entity_type = SUPPLIER


class FakeServiceTokenAuthentication(TokenAuthentication):

    def authenticate(self, request):
        return self.authenticate_credentials(None)

    def authenticate_credentials(self, key):
        return fake_authentication.get_authenticated_user(), None


fake_authentication = FakeUserAuthentication()
