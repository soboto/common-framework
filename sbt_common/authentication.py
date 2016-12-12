# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from grpc.beta import implementations
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

from protobuf.generated import users_pb2
from sbt_common.settings import api_settings
from sbt_common.utils import import_class


class ServiceTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        channel = implementations.insecure_channel('sbtbackoffice_users-50050', 50050)
        stub = users_pb2.beta_create_UsersService_stub(channel)
        response = stub.ValidateAuthenticationToken(users_pb2.ValidateAuthenticationTokenRequest(token=key), 1)

        if response.valid:
            user_info = response.user
            auth_model_interface = self.get_auth_model_interface_class()
            user = auth_model_interface().get_model(user_info)

            return user, None
        else:
            raise AuthenticationFailed(_('Invalid token.'))

    def get_auth_model_interface_class(self):
        return import_class(api_settings.AUTH_MODEL_INTERFACE)


class UserIsAuthenticated(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if api_settings.REQUIRE_AUTH is False:
            return True

        return super(self.__class__, self).has_permission(request, view)
