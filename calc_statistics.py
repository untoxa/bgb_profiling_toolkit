#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sts=4 sw=4 et
# Description: profiling stat calculator
# Author: Tony Pavlov (untoxa)
# SPDX-License-Identifier: MIT

import sys
import math
import functools

from BGB_toolkit import load_nogmb_symbols, calc_profiling_stats

def percentile(N, percent, key=lambda x:x):
    """
    Find the percentile of a list of values.

    @parameter N - is a list of values. Note N MUST BE already sorted.
    @parameter percent - a float value from 0.0 to 1.0.
    @parameter key - optional key function to compute value from each element of N.

    @return - the percentile of the values
    """
    if not N:
        return None
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

def calc_percentile(N, percent):
    N.sort()
    return percentile(N, percent)

if len(sys.argv) < 2:
    exit('USAGE: profile.py <profiler_log> <symbols>')

# loading symbols
symbols = load_nogmb_symbols(sys.argv[2], resolve_banks=True) if len(sys.argv) > 2 else {}
   
# calculating the stat
stat = calc_profiling_stats(sys.argv[1], double_speed=False, all_data=True, symbols=symbols)

# pretty-print the stat
for k,v in stat.items():
    print('{:50s} MIN:{:-8d} AVG:{:-10.2f} 95P:{:-8.0f} MAX:{:-8d}   TOTAL: {:s} NCALLS: {:d}'.format(k, v['min'], v['totalclk'] / v['ncalls'], calc_percentile(v['data'], 0.95), v['max'], '0x{:016x}'.format(v['totalclk']), v['ncalls']))
