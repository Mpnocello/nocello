from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import time

def pad(text):
    padding_value = 8 - (len(text) % 8)
    return text + bytes([padding_value] * padding_value)

def unpad(text):
    padding_value = text[-1]
    return text[:-padding_value]

def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plain_text))

def decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(cipher_text))