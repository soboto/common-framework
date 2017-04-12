from sbt_common.authentication import UserIsAuthenticated
from sbt_common.auth.permissions import ServiceModelPermissions


class CustomAuthenticationViewMixin(object):
    auth_actions = None
    permission_classes = []

    # http://stackoverflow.com/a/30624527
    def get_permissions(self):
        if self.action in self.auth_actions:
            self.permission_classes += (UserIsAuthenticated, )
        else:
            self.permission_classes = ()

        return super(CustomAuthenticationViewMixin, self).get_permissions()


class PermissionsViewMixin(object):
    model_permissions = None
    permission_classes = (UserIsAuthenticated, ServiceModelPermissions,)
