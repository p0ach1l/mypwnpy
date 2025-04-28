import sys
import re
from pwn import remote, process ,gdb

def pr(url=None, filename=None, debug=False , gdbscript=None):
    remote_mode = False
    local_mode = False

    if len(sys.argv) > 1:
        if sys.argv[1] == 're':  # 远程连接
            remote_mode = True
        elif sys.argv[1] == 'de':  # 本地调试
            local_mode = True
            debug = True

    if remote_mode and url:
        match = re.match(r'([^:\s]+)(?::(\d+)|\s+(\d+))?', url)
        hostname, port = (match.group(1), match.group(2) or match.group(3)) if match else (None, None)
        p = remote(hostname, port)
    else:
        p = process(filename)

    if debug:
        if isinstance(p, process):
            gdb.attach(p, gdbscript=gdbscript)
            print("GDB attached successfully")

    return p
