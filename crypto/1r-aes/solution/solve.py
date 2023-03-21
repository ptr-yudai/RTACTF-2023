from ptrlib import *
from aes import matrix2bytes, bytes2matrix, inv_shift_rows
import os

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "7003"))

sock = Socket(HOST, PORT)
#sock = Process(["python", "../distfiles/server.py"])

flag_enc = bytes.fromhex(sock.recvlineafter("enc(la): ").decode())
print("enc(flag):", flag_enc.hex())

def encrypt(m):
    sock.sendlineafter("msg > ", m.hex())
    msg_enc = bytes.fromhex(sock.recvlineafter("enc(msg): ").decode())
    m = bytes2matrix(msg_enc)
    inv_shift_rows(m)
    return matrix2bytes(m)

t = bytes2matrix(flag_enc)
inv_shift_rows(t)
t = matrix2bytes(t)

flag = ["?" for i in range(16)]
restored = 0

for c in table_large:
    r = encrypt((c * len(flag)).encode())
    for i in range(len(flag)):
        if r[i] == t[i]:
            flag[i] = c

print(f"RTACTF{{{''.join(flag)}}}")
sock.close()
