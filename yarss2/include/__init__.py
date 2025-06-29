# -*- coding: utf-8 -*-
#
# Copyright (C) 2012-2015 bendikro bro.devel+yarss2@gmail.com
#
# This file is part of YaRSS2 and is licensed under GNU General Public License 3.0, or later, with
# the additional special exception to link portions of this program with the OpenSSL library.
# See LICENSE for more details.
#

import os
import sys

# Add the include directory to sys.path so bundled libraries can find each other
include_dir = os.path.dirname(__file__)
if include_dir not in sys.path:
    sys.path.insert(0, include_dir)

# Import and expose the six module so other libraries can find it
try:
    from . import six
    sys.modules['six'] = six
except ImportError:
    pass
