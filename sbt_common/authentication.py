# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import get_authorization_header
from sbt_common.messaging.service import Service

from .protobuf import ProtoService
from .settings import api_settings
from .utils import import_class
from .models import Anonymous


class ServiceTokenAuthentication(TokenAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth:
            return self.authenticate_credentials(None)

        return super(ServiceTokenAuthentication, self).authenticate(request)

    def authenticate_credentials(self, key):
        if not key:
            return Anonymous(), None

        users_service = Service('users')
        response = users_service.validateAuthenticationToken({'token': key})

        if response.valid:
            user_info = response.user
            user_factory = self.get_user_factory()
            user = user_factory(user_info).get_user()

            return user, None
        else:
            raise AuthenticationFailed(_('Invalid token.'))

    def get_user_factory(self):
        return import_class(api_settings.AUTH_MODEL_FACTORY)


class UserIsAuthenticated(IsAuthenticated):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if api_settings.REQUIRE_AUTH is False:
            return True

        return super(self.__class__, self).has_permission(request, view)
