import aes
import os

key = os.getenv("KEY", "*** REDACTED ***").encode()
assert len(key) == 16

flag = os.getenv("FLAG", "RTACTF{9876000000001234}") # Find me
assert flag.startswith("RTACTF{") and flag.endswith("}")
la = flag[len("RTACTF{"):-len("}")]
assert len(la) == 16 and la.isnumeric()

cipher = aes.AES(key)
print("enc(la):", cipher.encrypt_block(la.encode()).hex())

while True:
    cipher = aes.AES(key)
    plaintext = bytes.fromhex(input("msg > "))
    assert len(plaintext) == 16
    print("enc(msg):", cipher.encrypt_block(plaintext).hex())
