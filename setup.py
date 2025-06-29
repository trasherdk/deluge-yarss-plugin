# -*- coding: utf-8 -*-
#
# Copyright (C) 2012-2015 bendikro bro.devel+yarss2@gmail.com
#
# Based on work by:
# Copyright (C) 2009 Camillo Dell'mour <cdellmour@gmail.com>
#
# This file is part of YaRSS2 and is licensed under GNU General Public License 3.0, or later, with
# the additional special exception to link portions of this program with the OpenSSL library.
# See LICENSE for more details.
#

import sys
from setuptools import find_packages, setup

__plugin_name__ = "YaRSS2"
__author__ = "Bro"
__author_email__ = "bro.devel+yarss2@gmail.com"
__version__ = "2.2.0"
__url__ = "http://dev.deluge-torrent.org/wiki/Plugins/YaRSS2"
__license__ = "GPLv3"
__description__ = "Yet another RSS 2"
__long_description__ = """
Yet another RSS 2, a simple RSS plugin for Deluge, based on
YaRSS written by Camillo Dell'mour <cdellmour@gmail.com>.
Tested with Deluge 2.0.3.
"""

# Print build info
print(f"Building YaRSS2 version {__version__}")

__pkg_data__ = {__plugin_name__.lower(): ["data/*"]}
packages = find_packages(exclude=[
    "yarss2.tests",
    "yarss2.include.beautifulsoup.bs4*",
    "yarss2.include.beautifulsoup.scripts*"
])

setup(
    name=__plugin_name__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    long_description=__long_description__ if __long_description__ else __description__,
    python_requires=">=3.9",
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Communications :: File Sharing",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
    ],
    include_package_data=True,
    packages=packages,
    package_data=__pkg_data__,
    entry_points="""[deluge.plugin.core]
%s = %s:CorePlugin
[deluge.plugin.gtkui]
%s = %s:GtkUIPlugin
[deluge.plugin.web]
%s = %s:WebUIPlugin
[deluge.plugin.gtk3ui]
%s = %s:Gtk3UIPlugin
[yarss2.libpaths]
include = yarss2.include
six = yarss2.include.six
requests = yarss2.include.requests
dateutil = yarss2.include.dateutil
defusedxml = yarss2.include.defusedxml
beautifulsoup = yarss2.include.beautifulsoup.py3k
atoma = yarss2.include.atoma
html5lib = yarss2.include.html5lib
webencodings = yarss2.include.webencodings
urllib3 = yarss2.include.urllib3.src
certifi = yarss2.include.certifi
""" % ((__plugin_name__, __plugin_name__.lower()) * 4))
