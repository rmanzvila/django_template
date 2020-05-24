# -*- coding: utf-8 -*-


def clean_boolean(item=None):
    """Parses a 'true' string to a boolean."""
    if item is not None:
        if isinstance(item, str):
            return True if item == 'true' else False
        elif isinstance(item, bool):
            return item
    return False
