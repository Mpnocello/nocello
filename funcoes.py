from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import time

# Função para adicionar padding ao texto de entrada. 
# Isso garante que o tamanho do texto seja múltiplo de 8 bytes, conforme necessário pelo DES.
def pad(text):
    # Calcula quantos bytes de padding são necessários.
    padding_value = 8 - (len(text) % 8)
    
    # Adiciona bytes de padding ao final do texto. O valor do byte de padding é o próprio número de bytes que precisam ser adicionados.
    return text + bytes([padding_value] * padding_value)

# Função para remover o padding de um texto de entrada.
def unpad(text):
    # Pega o valor do último byte, que indica a quantidade de bytes de padding.
    padding_value = text[-1]
    
    # Remove os bytes de padding do final do texto.
    return text[:-padding_value]

# Função para criptografar um texto usando o algoritmo DES.
def encrypt(plain_text, key):
    # Cria um novo objeto de criptografia DES no modo ECB.
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Criptografa o texto (depois de adicionar padding) e retorna o texto cifrado.
    return cipher.encrypt(pad(plain_text))

# Função para descriptografar um texto cifrado usando o algoritmo DES.
def decrypt(cipher_text, key):
    # Cria um novo objeto de criptografia DES no modo ECB.
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Descriptografa o texto cifrado e remove o padding antes de retornar o texto original.
    return unpad(cipher.decrypt(cipher_text))
