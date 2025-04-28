import inspect
from pwn import log

def ls(data):
    log.success(data)

def lss(s):
    frame = inspect.currentframe().f_back
    value = frame.f_locals.get(s)
    if value is None:
        ls("Variable '%s' not found." % s)
    else:
        ls('\033[1;31;40m%s ---> 0x%x \033[0m' % (s, value))
