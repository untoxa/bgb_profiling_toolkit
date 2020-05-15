#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sts=4 sw=4 et
# Description: profiling stat calculator
# Author: Tony Pavlov (untoxa)
# SPDX-License-Identifier: MIT

import sys

from BGB_toolkit import load_nogmb_symbols, calc_profiling_stats


if len(sys.argv) < 2:
    exit('USAGE: profile.py <profiler_log> <symbols>')

# loading symbols
symbols = load_nogmb_symbols(sys.argv[2], resolve_banks=True) if len(sys.argv) > 2 else {}
   
# calculating the stat
stat = calc_profiling_stats(sys.argv[1], double_speed=False, symbols=symbols)

# pretty-print the stat
for k,v in stat.items():
    print('{:50s} MIN:{:-8d} AVG:{:-10.2f} MAX:{:-8d}   TOTAL: {:s} NCALLS: {:d}'.format(k, v['min'], v['totalclk'] / v['ncalls'], v['max'], '0x{:016x}'.format(v['totalclk']), v['ncalls']))
