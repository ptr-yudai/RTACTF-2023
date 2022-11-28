from ptrlib import xor, chunks

with open("../distfiles/output.txt", "r") as f:
    f.seek(len("Encrypted: "))
    c = bytes.fromhex(f.read())
iv, cipher = c[:8], c[8:]

key_head = xor(xor(cipher[:7], iv), "RTACTF{")
for c in range(0x100):
    key = key_head + bytes([c])

    temp_iv = iv
    plain = b''
    for block in chunks(cipher, 8):
        plain += xor(xor(block, temp_iv), key)
        temp_iv = block

    if plain[-1] <= 8 and plain[-plain[-1]:] == plain[-1:]*plain[-1]:
        flag = plain[:-plain[-1]]
        if flag.startswith(b"RTACTF{") and flag.endswith(b"}"):
            print(key)
            print(flag.decode())
