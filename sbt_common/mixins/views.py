from sbt_common.authentication import UserIsAuthenticated


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
