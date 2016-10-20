# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from grpc.beta import implementations
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

from protobuf.generated import users_pb2
from sbt_common.settings import api_settings


class AuthUser(object):
    username = None
    user_id = None
    name = None

    def __init__(self, username, user_id, name, *args, **kwargs):
        self.username = username
        self.user_id = user_id
        self.name = name

    def __unicode__(self):
        return self.username

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self


class ServiceTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):

        channel = implementations.insecure_channel('sbtbackoffice_users-50050', 50050)
        stub = users_pb2.beta_create_UsersService_stub(channel)
        response = stub.ValidateAuthenticationToken(users_pb2.ValidateAuthenticationTokenRequest(token=key), 1)

        if response.valid:
            user_info = response.auth_user
            user = AuthUser(user_info.username, user_info.user_id, user_info.name)

            return user, None
        else:
            raise AuthenticationFailed(_('Invalid token.'))


class UserIsAuthenticated(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if api_settings.REQUIRE_AUTH is False:
            return True

        return super(self.__class__, self).has_permission(request, view)
