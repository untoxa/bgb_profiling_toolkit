#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sts=4 sw=4 et
# Description: BGB snapshot logger
# Author: Tony Pavlov (untoxa)
# SPDX-License-Identifier: MIT

import sys
from array import array

from BGB_toolkit import read_bgb_snspshot

# read the snapshot to the dict
snapshot = read_bgb_snspshot(sys.argv[1])

# pretty-print the snapshot dict
for k, v in snapshot.items():
    if v is None: 
        print(k)
    elif type(v) is array:
        if len(v) <= 16:
            print("{:20s}: [{:s}]".format(k, ', '.join(['0x{:02x}'.format(x) for x in v])))
        else:
            print("{:20s}: ARRAY[{:d}]".format(k, len(v)))
    elif type(v) is list:
        print("{:20s}: 0x{:0{}x}".format(k, v[1], v[0] * 2))
