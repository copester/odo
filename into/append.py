from __future__ import absolute_import, division, print_function

from multipledispatch import Dispatcher
from .convert import convert

append = Dispatcher('append')

@append.register(list, list)
def list_to_list(a, b, **kwargs):
    a.extend(b)
    return a


@append.register(list, object)
def list_to_list(a, b, **kwargs):
    a.extend(convert(list, b))
    return a


@append.register(set, set)
def set_to_set(a, b, **kwargs):
    a.update(b)
    return a


@append.register(set, object)
def set_to_set(a, b, **kwargs):
    a.update(convert(set, b))
    return a