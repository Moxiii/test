from Crypto.Cipher import AES
from Crypto import Random
import hashlib
from cryptography.fernet import Fernet
Pass = Fernet.generate_key()
key = hashlib.sha256(Pass).digest()
mode = AES.MODE_CBC
saut = "\n"
print("clé:" , Pass)
print("Clé hasher : " ,key)
IV = Random.new().read(AES.block_size)
print("LE FAMEUX IV",IV)
cipher = AES.new(key,mode)
with open('FILE/PLAIN/test.txt' , 'rb') as file:
    file.read()
message = "message to encode"
print(len(message), message)
# ressource : https://medium.com/swlh/an-introduction-to-the-advanced-encryption-standard-aes-d7b72cc8de97