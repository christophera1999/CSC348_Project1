# /*
#  * Copyright (c) 2024.
#  * Author: Christopher Atala
#  * Due Date: 02/01/2024
#  * Program explores encryption and decryption using ciphers
#  * Program Assignment #1 - Part 1 of 2
#  */

# 1.1 Caesar Cipher - shift the letters by a certain amount
def caesar_cipher(message, shift, encrypt):
    out = ''
    for char in message:
        if encrypt:
            out = out + chr((ord(char) + shift - 32) % 95 + 32) #if encrypting, add the shift and wrap around
        else:
            out = out + chr((ord(char) - shift - 32) % 95 + 32) #if decrypting, subtract the shift and wrap around
    return out

# 1.2 Vigenere Cipher - shift the letters by a certain amount, but the amount is determined by the keyword
def vigenere_cipher(message, keyword, encrypt):
    out = ''
    for i in range(len(message)):
        out = out + caesar_cipher(message[i], ord(keyword[i % len(keyword)]) - 32, encrypt) #if encrypting, add the shift
    return out

if __name__ == '__main__':
    # 1.1 Caesar Cipher
    encrypt = caesar_cipher('hello world', 5, True)
    decrypt = caesar_cipher(encrypt, 5, False)

    print(encrypt)
    print(decrypt)

    # 1.2 Vigenere Cipher

    encrypt = vigenere_cipher('Hello World!', 'cake', True)
    decrypt = vigenere_cipher(encrypt, 'cake', False)

    print(encrypt)
    print(decrypt)