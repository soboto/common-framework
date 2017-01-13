# -*- coding: utf-8 -*-
from rest_framework.permissions import DjangoModelPermissions


class ServiceModelPermissions(DjangoModelPermissions):

    perms_map = {
        'GET': ['%(model_name)s.view'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(model_name)s.add'],
        'PUT': ['%(model_name)s.edit'],
        'PATCH': ['%(model_name)s.edit'],
        'DELETE': ['%(model_name)s.remove'],
    }

    def get_required_permissions(self, method, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        model_name = getattr(self._view, 'model_permissions', model_cls._meta.model_name)
        kwargs = {
            'model_name': model_name
        }
        return [perm % kwargs for perm in self.perms_map[method]]

    def has_permission(self, request, view):
        self._view = view

        if hasattr(view, 'perms_map'):
            self.perms_map.update(view.perms_map)

        return super(ServiceModelPermissions, self).has_permission(request, view)
