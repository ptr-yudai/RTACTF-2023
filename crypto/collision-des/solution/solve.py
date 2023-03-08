from ptrlib import *
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "7002"))

sock = Socket(HOST, PORT)

key1 = bytes.fromhex(sock.recvlineafter("Key 1: ").decode())
key2 = b''.join(map(lambda c: bytes([c ^ 1]), list(key1)))
sock.sendlineafter("Key 2: ", key2.hex())

sock.sh()
