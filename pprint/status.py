#!/usr/bin/env python3

from color import ColorStr

def print_successful(msg):
    sucess = ColorStr("[+]")
    print(f"{sucess.ForeGREEN} {msg}")
    
def print_status(msg):
    status = ColorStr("[*]")
    print(f"{status.ForeCYAN} {msg}")

def print_failure(msg):
    failure = ColorStr("[-]")
    print(f"{failure.ForeRED} {msg}")
