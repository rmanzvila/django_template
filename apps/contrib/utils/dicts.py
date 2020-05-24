# -*- coding: utf-8 -*-


def lower_dict_values(dict_obj):
    """Returns a lower case version of a dict."""
    new_dict = {}
    for key, value in dict_obj.items():
        _value = value
        if isinstance(value, str):
            _value = _value.lower()
        new_dict[key] = _value
    return new_dict
