from ptrlib import *
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "7001"))

def encrypt(msg):
    sock = Socket(HOST, PORT)
    a = bytes.fromhex(sock.recvline().decode())
    sock.sendlineafter("> ", msg)
    b = bytes.fromhex(sock.recvline().decode())
    sock.close()
    return a, b

# Get ciphertext length
a, _ = encrypt("hoge")
length = len(a)

# Break cipher
flag = ''
for i in range(length):
    logger.info(f"Leaking {i+1}/{length}")
    a, b = encrypt(flag.encode() + b'\x00' * (length - i))
    flag += chr(xor(a, b)[i])

print(flag)
