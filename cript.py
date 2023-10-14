from Crypto.Random import get_random_bytes

from funcoes import *

key = get_random_bytes(8)
plain_text = input('Escreva a mensagem:').encode() 

encrypted_message = encrypt(plain_text, key)
decrypted_message = decrypt(encrypted_message, key)

print("Mensagem Original:", plain_text)
print("Mensagem Encriptada:", encrypted_message.hex())
print("Mensagem Decriptada:", decrypted_message.decode())
