Profiling toolkit for SDCC and BGB
==================================

pre-requirements:
=================

1. GBDK-2020 v3.1 or higher: https://github.com/Zal0/gbdk-2020/releases
2. you must #include <gb/bgb_emu.h> in your main source; this enables linking the features, described above
3. your C-program must be compiled with SDCC "--profile" switch 
4. you must also switch on saving debug messages into the file in your BGB emulator:
![BGB settings](/bgb_settings.png)

BGB_toolkit.py contains these helper functions:
===============================================

load_noi
--------

    symbols = load_noi(filename)

parses the *.noi symbol file, that is produced by sdldgb linker

    filename        : path and filename to *.noi symbols file

function returns the address->symbol dict

load_nogmb_map
--------------

    symbols = load_nogmb_map(filename)

parses the *.map file in no$gmb format, that is produced by link-gbz80 linker

    filename        : path and filename to *.map symbols file

function returns the address->symbol dict

load_nogmb_symbols
------------------

    symbols = load_nogmb_symbols(filename, resolve_banks=False)

parses the *.sym file in no$gmb format, that is produced by link-gbz80 linker

    filename        : path and filename to *.sym symbols file
    resolve_banks   : optional parameter that allows to extract bank numbers from the comments in *.sym file; 
                      False by default

function returns the address->symbol dict

calc_profiling_stats
--------------------

    stats = calc_profiling_stats(filename, double_speed=False, all_data=False, symbols={})

parses the BGB "debug messages" log file and calculate profiling stat

    filename        : path and filename to the BGB log file
    double_speed    : set to True if cpu_fast() is called; False by default
    all_data        : set to True if all avaliable data is required in result
    symbols         : optional symbols dict as returned by load_nogmb_symbols; empty dict by default

function returns the stat dict where call trace is a key and node-stat dict for this trace is a value.

node-stat dict contains:
    
    {'ncalls': ncalls, 'totalclk': totalclk, 'min': min, 'max': max, 'data': []}
    
where: 
    
    ncalls      : number of calls
    totalclk    : total amount of cycles
    min         : minumum number of cycles of this call
    max         : maximum number of cycles of this call
    data        : list of all measures for this trace (if all_data parameter is set to True)

example output without symbols loaded:
![statistics2](/screenshot2.png)

with symbols loaded:
![statistics1](/screenshot1.png)

read_bgb_snspshot
-----------------

    snapshot = read_bgb_snspshot(filename)

loads the BGB snapshot file into the dict

    filename : path and file name of a snapshot file produced by BGB emulator

function returns a dict, that contains this snapshot. keys of this dict are string ID's, that identify the data, and
values are either None, Array or [len, Data] list where Data is an integer value; please, examine the log_snapshot.py
example source and output for the details.
