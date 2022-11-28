from ptrlib import *

sock = Process(["python", "../distfiles/server.py"])

key1 = bytes.fromhex(sock.recvlineafter("Key 1: ").decode())
key2 = b''.join(map(lambda c: bytes([c ^ 1]), list(key1)))
sock.sendlineafter("Key 2: ", key2.hex())

sock.sh()
