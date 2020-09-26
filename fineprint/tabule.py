#!/usr/bin/env python3
from tabulate import tabulate

def search_table(table_data, search_parameter):
    pass

def print_table(table_data, *,  headers=(), color_headers=None,
                tablefmt='simple', floatfmt='g', numalign='decimal', 
                stralign='left', missingval='', showindex='default', 
                disable_numparse=False, colalign=None):
    # add color headers support
    formatted_table = tabulate(table_data,headers=headers,
            tablefmt=tablefmt, floatfmt=floatfmt, numalign=numalign, 
            stralign=stralign, missingval=missingval, showindex=showindex, 
            disable_numparse=disable_numparse, colalign=colalign)
    print(formatted_table)