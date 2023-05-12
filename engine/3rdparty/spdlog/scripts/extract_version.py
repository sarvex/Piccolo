#!/usr/bin/env python3

import os
import re

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_h = os.path.join(base_path, 'include', 'spdlog', 'version.h')
data = {'MAJOR': 0, 'MINOR': 0, 'PATCH': 0}
reg = re.compile(r'^\s*#define\s+SPDLOG_VER_([A-Z]+)\s+([0-9]+).*$')

with open(config_h, 'r') as fp:
    for l in fp:
        if m := reg.match(l):
            data[m[1]] = int(m[2])

print(f"{data['MAJOR']}.{data['MINOR']}.{data['PATCH']}")
