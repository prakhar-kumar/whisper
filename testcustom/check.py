import re

file = open('mem.log', 'r')

last_addr = 0
last_diff = 0
last_bp = False

for line in file:
    cols = re.split(r'\s+', line.strip(), maxsplit=7)
    addr = int(cols[5], 16) 
    value = int(cols[6], 16)

    diff = addr - last_addr
    bp = diff != last_diff or value != 0

    if bp and not last_bp:
        print('BREAK', hex(last_addr), last_diff, bp, last_bp)    
    elif last_bp and not bp:
        print('START', hex(addr), last_diff, bp, last_bp)
    else:
        print('NORMA', hex(addr), last_diff, bp, last_bp)

    last_addr = addr
    last_diff = diff
    last_bp = bp