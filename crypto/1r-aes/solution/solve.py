from ptrlib import *
from aes import matrix2bytes, bytes2matrix, inv_shift_rows
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "7003"))

sock = Socket(HOST, PORT)

flag_enc = bytes.fromhex(sock.recvlineafter("enc(la): ").decode())
print("enc(flag):", flag_enc.hex())

def encrypt(val):
    sock.sendlineafter("msg > ", int.to_bytes(val, 16, 'big').hex())
    msg_enc = bytes.fromhex(sock.recvlineafter("enc(msg): ").decode())
    m = bytes2matrix(msg_enc)
    inv_shift_rows(m)
    m = int.from_bytes(matrix2bytes(m), 'big')
    return m

t = bytes2matrix(flag_enc)
inv_shift_rows(t)
t = int.from_bytes(matrix2bytes(t), 'big')

flag = ""
restored = 0
for i in range(16):
    for c in range(0x30, 0x3a):
        if encrypt(restored|(c<<(i*8))) & (0xff<<(i*8)) == t & (0xff<<(i*8)):
            restored |= c << (i*8)
            flag += chr(c)
            print(flag)
            break

print(flag[::-1])
sock.close()
