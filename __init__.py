# flake8: noqa

import logging
import sys
import inspect
from PyQt5 import Qt
from PyQt5.QtCore import QT_VERSION_STR


__appname__ = "labelme"

# Semantic Versioning 2.0.0: https://semver.org/
# 1. MAJOR version when you make incompatible API changes;
# 2. MINOR version when you add functionality in a backwards-compatible manner;
# 3. PATCH version when you make backwards-compatible bug fixes.
__version__ = "4.6.0"

QT4 = QT_VERSION_STR.split(".")[0] == "4"
QT5 =QT_VERSION_STR.split(".")[0] == "5"
del QT_VERSION_STR

PY2 = sys.version[0] == "2"
PY3 = sys.version[0] == "3"
del sys

