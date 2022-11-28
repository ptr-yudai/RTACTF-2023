from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

iv = os.urandom(16)
key = os.urandom(16)
FLAG = os.getenv("FLAG", "RTACTF{**** REDACTED ****}").encode()

def encrypt(data):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.encrypt(pad(data, 16))

if __name__ == '__main__':
    print(encrypt(FLAG).hex())
    print(encrypt(input("> ").encode()).hex())
