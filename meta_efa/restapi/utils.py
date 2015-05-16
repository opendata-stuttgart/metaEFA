import re

dromeda_pat = re.compile(r'([A-Z])')
under_pat = re.compile(r'_([a-z])')


def dromeda_to_underscore(name):
    return dromeda_pat.sub(lambda x: '_' + x.group(1).lower(), name)


def underscore_to_dromeda(name):
    return under_pat.sub(lambda x: x.group(1).upper(), name)
