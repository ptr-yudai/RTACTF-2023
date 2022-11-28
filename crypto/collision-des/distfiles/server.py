from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import os

FLAG = os.getenv("FLAG", "RTACTF{**** REDACTED ****}")

def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, 8))

if __name__ == '__main__':
    key1 = os.urandom(8)
    print(f"Key 1: {key1.hex()}")
    key2 = bytes.fromhex(input("Key 2: "))

    assert len(key1) == len(key2) == 8, "Invalid key size :("
    assert len(set(key1).intersection(set(key2))) == 0, "Keys look similar :("

    plaintext = b"The quick brown fox jumps over the lazy dog."
    if encrypt(key1, plaintext) == encrypt(key2, plaintext):
        print("[+] You found a collision!")
        print(FLAG)
    else:
        print("[-] Nope.")
