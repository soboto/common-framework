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

    def get_required_permissions(self, method, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        model_name = getattr(self._view, 'model_permissions', model_cls._meta.model_name)
        action = self._view.action
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

    def has_permission(self, request, view):
        self._view = view

        if hasattr(view, 'perms_map'):
            self.perms_map.update(view.perms_map)

        return super(ServiceModelPermissions, self).has_permission(request, view)
