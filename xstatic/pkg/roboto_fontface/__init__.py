
"""
XStatic resource package

See package 'XStatic' for documentation and basic tools.
"""

# official name, upper/lowercase allowed, no spaces
DISPLAY_NAME = 'roboto-fontface'

# name used for PyPi
PACKAGE_NAME = 'XStatic-%s' % DISPLAY_NAME

NAME = __name__.split('.')[-1] # package name (e.g. 'foo' or 'foo_bar')
                               # please use a all-lowercase valid python
                               # package name

VERSION = '0.8.0' # version of the packaged files, please use the upstream
                  # version number
BUILD = '1' # our package build number, so we can release new builds
             # with fixes for xstatic stuff.
PACKAGE_VERSION = VERSION + '.' + BUILD # version used for PyPi

DESCRIPTION = "%s %s (XStatic packaging standard)" % (DISPLAY_NAME, VERSION)

PLATFORMS = 'any'
CLASSIFIERS = []
KEYWORDS = 'roboto_fontface xstatic'

# XStatic-* package maintainer:
MAINTAINER = 'Rob Cresswell'
MAINTAINER_EMAIL = 'robert.cresswell@outlook.com'

# this refers to the project homepage of the stuff we packaged:
HOMEPAGE = 'https://github.com/choffmeister/roboto-fontface-bower'

# this refers to all files:
LICENSE = 'Apache-2.0'

from os.path import join, dirname
BASE_DIR = join(dirname(__file__), 'data')
# linux package maintainers just can point to their file locations like this:
#BASE_DIR = '/usr/share/javascript/' + NAME

# location of the Javascript file that's the entry point for this package, if
# one exists, relative to BASE_DIR
MAIN="[u'./css/roboto-fontface.css', u'./fonts/Roboto-Black.eot', u'./fonts/Roboto-Black.svg', u'./fonts/Roboto-Black.ttf', u'./fonts/Roboto-Black.woff', u'./fonts/Roboto-Black.woff2', u'./fonts/Roboto-BlackItalic.eot', u'./fonts/Roboto-BlackItalic.svg', u'./fonts/Roboto-BlackItalic.ttf', u'./fonts/Roboto-BlackItalic.woff', u'./fonts/Roboto-BlackItalic.woff2', u'./fonts/Roboto-Bold.eot', u'./fonts/Roboto-Bold.svg', u'./fonts/Roboto-Bold.ttf', u'./fonts/Roboto-Bold.woff', u'./fonts/Roboto-Bold.woff2', u'./fonts/Roboto-BoldItalic.eot', u'./fonts/Roboto-BoldItalic.svg', u'./fonts/Roboto-BoldItalic.ttf', u'./fonts/Roboto-BoldItalic.woff', u'./fonts/Roboto-BoldItalic.woff2', u'./fonts/Roboto-Light.eot', u'./fonts/Roboto-Light.svg', u'./fonts/Roboto-Light.ttf', u'./fonts/Roboto-Light.woff', u'./fonts/Roboto-Light.woff2', u'./fonts/Roboto-LightItalic.eot', u'./fonts/Roboto-LightItalic.svg', u'./fonts/Roboto-LightItalic.ttf', u'./fonts/Roboto-LightItalic.woff', u'./fonts/Roboto-LightItalic.woff2', u'./fonts/Roboto-Medium.eot', u'./fonts/Roboto-Medium.svg', u'./fonts/Roboto-Medium.ttf', u'./fonts/Roboto-Medium.woff', u'./fonts/Roboto-Medium.woff2', u'./fonts/Roboto-MediumItalic.eot', u'./fonts/Roboto-MediumItalic.svg', u'./fonts/Roboto-MediumItalic.ttf', u'./fonts/Roboto-MediumItalic.woff', u'./fonts/Roboto-MediumItalic.woff2', u'./fonts/Roboto-Regular.eot', u'./fonts/Roboto-Regular.svg', u'./fonts/Roboto-Regular.ttf', u'./fonts/Roboto-Regular.woff', u'./fonts/Roboto-Regular.woff2', u'./fonts/Roboto-RegularItalic.eot', u'./fonts/Roboto-RegularItalic.svg', u'./fonts/Roboto-RegularItalic.ttf', u'./fonts/Roboto-RegularItalic.woff', u'./fonts/Roboto-RegularItalic.woff2', u'./fonts/Roboto-Thin.eot', u'./fonts/Roboto-Thin.svg', u'./fonts/Roboto-Thin.ttf', u'./fonts/Roboto-Thin.woff', u'./fonts/Roboto-Thin.woff2', u'./fonts/Roboto-ThinItalic.eot', u'./fonts/Roboto-ThinItalic.svg', u'./fonts/Roboto-ThinItalic.ttf', u'./fonts/Roboto-ThinItalic.woff', u'./fonts/Roboto-ThinItalic.woff2']"

LOCATIONS = {
    # CDN locations (if no public CDN exists, use an empty dict)
    # if value is a string, it is a base location, just append relative
    # path/filename. if value is a dict, do another lookup using the
    # relative path/filename you want.
    # your relative path/filenames should usually be without version
    # information, because either the base dir/url is exactly for this
    # version or the mapping will care for accessing this version.
}
