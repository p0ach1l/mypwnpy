import sys
import re
from pwn import *

def pr(url=None, filename=None,  gdbscript=None , framepath = None):
    p = None

    remote_mode = len(sys.argv) > 1 and sys.argv[1] == 're'
    debug_mode = len(sys.argv) > 1 and sys.argv[1] == 'de'

    if remote_mode:
        if not url:
            log.error("Remote mode requires a URL (format: host:port)")
        match = re.match(r'([^:\s]+)(?::(\d+)|\s+(\d+))?', url)
        if not match:
            log.error(f"Invalid URL format: {url}")
        hostname, port = (match.group(1), match.group(2) or match.group(3)) if match else (None, None)
        p = remote(host, port)

    else:
        if not filename:
            log.error("Local mode requires a filename")
        
        arch = context.arch

        qemu_archs = ['arm', 'aarch64', 'mips', 'mipsel']
        if arch in qemu_archs:
            args = ['qemu-' + arch , '-L' , framepath]
            if debug_mode:
                args += ['-g', '1234']
            args.append(filename)
            p = process(args)
        else:
            p = process(filename)
            if debug_mode:
                gdb.attach(p, gdbscript=gdbscript)
                log.info("GDB attached successfully")

    return p
