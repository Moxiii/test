from ctypes.wintypes import PDWORD
import tkinter
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad , unpad
import hashlib
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from cryptography.fernet import Fernet
import os, os.path
from tkinter.filedialog import askopenfile, askopenfilename
Pass = Fernet.generate_key()
key = hashlib.sha256(Pass).digest()
message=b"HELLO WOLRD"
password ="azerty"
key + PBKDF2(password,key,dkLen=32)
cipher = AES.new(key,AES.MODE_CBC)
data = cipher.encrypt(pad(message,AES.block_size))
print(data)
with open('encrypted.bin' ,'wb') as file:
    file.write(cipher.iv)
    file.write(data)

with open('encrypted.bin' , 'rb') as file :
    iv = file.read(16)
    decrypted = file.read()

cipher = AES.new(key , AES.MODE_CBC , iv=iv)



print('Please select option:\n1. Encryption\n2. Decryption\n3. Exit')

while True:
    user_choice = input("Choose a option: ")
    if user_choice == "1":
         file = askopenfilename()
         file_read=open(file,'r')
         data = cipher.encrypt(file_read,AES.block_size)
         print(key)


    elif user_choice == "2":
        print(file.read())
        original = unpad(cipher.decrypt(decrypted),AES.block_size)
        print(key)
    elif user_choice == "3":
        print("Quitting The Program....")
        break
    else:
        print("Please Choose a correct option")
