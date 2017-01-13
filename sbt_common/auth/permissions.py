# -*- coding: utf-8 -*-
from rest_framework.permissions import DjangoModelPermissions


class ServiceModelPermissions(DjangoModelPermissions):

    perms_map = {
        'GET': ['list_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['add_%(model_name)s'],
        'PUT': ['change_%(model_name)s'],
        'PATCH': ['change_%(model_name)s'],
        'DELETE': ['delete_%(model_name)s'],
    }

    def has_permission(self, request, view):

        if hasattr(view, 'perms_map'):
            self.perms_map.update(view.perms_map)

        return super(ServiceModelPermissions, self).has_permission(request, view)
