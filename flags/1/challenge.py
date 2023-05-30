# ctf2023 challenge one.

def flag(secret):
    e = "of_string)lpts{rotation_"
    return e[-secret:]+e[:-secret]

secret = 0

print("FLAG: " + flag(secret))