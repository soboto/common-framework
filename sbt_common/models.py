# -*- coding: utf-8 -*-
from protobuf_to_dict import protobuf_to_dict


class DefaultAuthModelInterface(object):

    def get_model(self, user_info):
        user_info = protobuf_to_dict(user_info)

        return AuthUser(**user_info)


class AuthUser(object):
    id = None
    username = None
    name = None
    first_name = None
    last_name = None
    email = None
    type = None
    entity = []

    def __init__(self, *args, **kwargs):
        for param in kwargs:
            setattr(self, param, kwargs.get(param))

        self.parse_entities()

    def parse_entities(self):
        self.entity = [e['id'] for e in self.entity]

    def __unicode__(self):
        return self.username

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self

    def _get_groups(self):
        return self._groups
    groups = property(_get_groups)

    def _get_user_permissions(self):
        return self._user_permissions
    user_permissions = property(_get_user_permissions)

    def get_group_permissions(self, obj=None):
        return set()

    def has_perms(self, perm_list, obj=None):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_username(self):
        return self.username
