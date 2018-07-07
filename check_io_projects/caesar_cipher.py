from pycipher import Caesar


def to_encrypt(text, delta):
    return Caesar(key=delta).encipher(text).lower()


print(to_encrypt("abc", 10))
