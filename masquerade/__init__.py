"""
django-masquerade
"""
__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 9,
    'releaselevel': 'final',
    'serial': 1
}

def get_version():
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()
