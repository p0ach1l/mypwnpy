# README

## 0x00

作为一个终极懒人，平常刷pwn题的各种模式切换显示十分繁琐，于是就诞生了这个小小的python库

用一个示例代码说明一下功能

```python
from pwn import *
from ctypes import *
from LibcSearcher import *
from pwnpy import *
import sys


filename = './pwn10'
url = ''
gdbscript = '''
  b * 0x00000000004008CB
'''
set_context()
p = pr(url = url , filename = filename , gdbscript = gdbscript)
elf = ELF(filename)
p.sendline(b'\x00')

p.interactive()
```



## 0x01 连接模块

1. 默认本地跑脚本

   ```python
   python pwn10.py
   ```

2. de调试模式

   ```python
   python pwn10.py de
   ```

   其中下断点填充gdbscript即可，支持多个断点同时下，以及各种pwndbg语法

3. re远端模式

   ```python
   python pwn10.py re
   ```

在拿到一个题只需要完善一下对应的filename、url就能快速刷题，丝滑切换各种模式

## 0x02 初始化context

通过调用set_context方法可以实现初始化set_context，可以根据个人习惯修改

```python
ef set_context(log_level='debug', arch='amd64', os='linux', endian='little', timeout=5):
    context.update(
        log_level=log_level, 
        arch=arch, 
        os=os, 
        endian=endian, 
        timeout=timeout, 
        terminal=['tmux', 'splitw', '-h', '-p', '80']
    )
```

