# -*- coding: utf-8 -*-
from rest_framework.permissions import DjangoModelPermissions


class ServiceModelPermissions(DjangoModelPermissions):

    perms_map = {
        'metadata': [],
        'retrieve': ['%(model_name)s.view'],
        'list': ['%(model_name)s.view'],
        'create': ['%(model_name)s.add'],
        'update': ['%(model_name)s.edit'],
        'partial_update': ['%(model_name)s.edit'],
        'destroy': ['%(model_name)s.remove'],
    }

    authenticated_users_only = False

    def has_permission(self, request, view):
        self._view = view

        if hasattr(view, 'perms_map'):
            self.perms_map.update(view.perms_map)

        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
        else:
            queryset = getattr(view, 'queryset', None)

        model_cls = queryset.model if queryset else None
        perms = self.get_required_permissions(request.method, model_cls)

        return (
            request.user and
            (request.user.is_authenticated() or not self.authenticated_users_only) and
            request.user.has_perms(perms)
        )

    def get_required_permissions(self, method, model_cls=None):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        default_model_name = model_cls._meta.model_name if model_cls else None
        model_name = getattr(self._view, 'model_permissions', default_model_name)

        action = getattr(self._view, 'action', None)
        action = action if action is not None else self._view.get_action()
        kwargs = {
            'model_name': model_name,
            'action': action
        }

        ignore_perm_actions = getattr(self._view, 'ignore_perm_actions', [])
        if action in ignore_perm_actions:
            return []

        if action in self.perms_map.keys():
            return [perm % kwargs for perm in self.perms_map[action]]
        else:
            return ['%(model_name)s.%(action)s' % kwargs]
