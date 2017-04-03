#!/usr/bin/env python3

import os
import os.path
import json

__author__ = 'Alexander Popov'
__version__ = '0.1.0'
__license__ = 'Unlicense'

PACKAGE_DIRS = list()

for item in os.listdir('./'):
    if not os.path.isfile(item):
        PACKAGE_DIRS.append(item)

if '.git' in PACKAGE_DIRS:
    PACKAGE_DIRS.remove('.git')

PACKAGES = list()

for package in PACKAGE_DIRS:
    with open('{0}/package.json'.format(package), 'r', encoding='utf-8') as f:
        PACKAGES.append(json.loads(f.read()))

with open('packages.json', 'w+', encoding='utf-8') as f:
    json.dump(PACKAGES, f) #, sort_keys=True, indent=4)
