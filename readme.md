Profiling toolkit for SDCC and BGB
==================================

BGB_toolkit.py contains these helper functions:

load_nogmb_symbols
------------------

    symbols = load_nogmb_symbols(filename, resolve_banks=False)

load the *.sym file in no$gmb format, that is produced by link-gbz80 linker

    filename        : path and filename to *.sym symbols file
    resolve_banks   : optional parameter that allows to extract bank numbers from the comments in *.sym file; 
                      False by default

function returns the address->symbol dict

calc_profiling_stats
--------------------

    stats = calc_profiling_stats(filename, double_speed=False, symbols={})

loads the BGB "debug messages" log file and calculates profiling stat

    filename        : path and filename to the BGB log file
    double_speed    : set to True if cpu_fast() is called; False by default
    symbols         : optional symbols dict as returned by load_nogmb_symbols; empty dict by default

function returns the stat dict where call trace is a key and node-stat dict for this trace is a value.

node-stat dict contains:
    
    {'ncalls': ncalls, 'totalclk': totalclk, 'min': min, 'max': max }
    
where: 
    
    ncalls      : number of calls
    totalclk    : total amount of cycles
    min         : minumum number of cycles of this call
    max         : maximum number of cycles of this call

![statistics](/screenshot.png)

read_bgb_snspshot
-----------------

    snapshot = read_bgb_snspshot(filename)

loads the BGB snapshot file into the dict

    filename : path and file name of a snapshot file produced by BGB emulator

function returns a dict, that contains this snapshot. keys of this dict are string ID's, that identify the data, and
values are either None, Array or [len, Data] list where Data is an integer value; please, examine the log_snapshot.py
example source and output for the details.

IMPORTANT: register pair values are big-endian!
