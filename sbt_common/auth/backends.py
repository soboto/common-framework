from django.contrib.auth.backends import ModelBackend

from ..protobuf import ProtoService
from ..settings import api_settings
from ..models import Anonymous


class ServiceModelBackend(ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def _get_user_permissions(self, user_obj):
        return set()

    def _get_group_permissions(self, user_obj):
        return None

    def _get_permissions(self, user_obj, obj, from_name):
        return None

    def get_user_permissions(self, user_obj, obj=None):
        """
        Returns a set of permission strings the user `user_obj` has from their
        `user_permissions`.
        """
        user_id = None
        if type(user_obj) is not Anonymous:
            user_id = str(user_obj.id)

        users_service = ProtoService(
            api_settings.SERVICE_USERS_URL,
            'users_pb2.beta_create_UsersService_stub'
        )
        response = users_service.execute(
            'getUserPermissions',
            'users_pb2.GetUserPermissionsRequest',
            {'user_id': user_id}
        )

        all_permissions = []
        for permission in response.permissions:
            all_permissions.append(permission.codename)

        return all_permissions

    def get_group_permissions(self, user_obj, obj=None):
        """
        Returns a set of permission strings the user `user_obj` has from the
        groups they belong.
        """
        return self._get_permissions(user_obj, obj, 'group')

    def get_all_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or obj is not None:
            return set()

        return self.get_user_permissions(user_obj, obj)

    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.is_superuser:
            return True

        return super(ServiceModelBackend, self).has_perm(user_obj, perm, obj)

    def get_user(self, user_id):
        return None
