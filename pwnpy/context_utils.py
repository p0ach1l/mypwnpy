from pwn import context

def set_context(log_level='debug', arch='amd64', os='linux', endian='little', timeout=5):
    context.update(
        log_level=log_level, 
        arch=arch, 
        os=os, 
        endian=endian, 
        timeout=timeout, 
        terminal=['tmux', 'splitw', '-h', '-p', '80']
    )
