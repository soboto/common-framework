from sbt_common.auth.backends import ServiceModelBackend


class FakeServiceModelBackend(ServiceModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def get_user_permissions(self, user_obj, obj=None):
        return []
