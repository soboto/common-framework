# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from grpc.beta import implementations
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from protobuf.generated import users_pb2


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


class UserAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):

        channel = implementations.insecure_channel('sbtbackoffice_sbt-users-50054', 50054)
        stub = users_pb2.beta_create_UsersService_stub(channel)
        response = stub.ValidateAuthenticationToken(users_pb2.ValidateAuthenticationTokenRequest(token=key), 1)

        if response.valid:
            user_info = response.auth_user
            user = AuthUser(user_info.username, user_info.user_id, user_info.name)

            return user, None
        else:
            raise AuthenticationFailed(_('Invalid token.'))
