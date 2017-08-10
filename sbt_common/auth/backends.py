from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from ..messaging.service import Service
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

        users_service = Service('users')
        response = users_service.getUserPermissions({'user_id': user_id})

        all_permissions = []
        for permission in response.permissions:
            all_permissions.append(permission.codename)

        # ====== For DEBUG =======
        # print user_obj.__dict__
        # print all_permissions

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
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
