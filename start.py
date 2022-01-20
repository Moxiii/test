from fileinput import filename
from lib2to3.pgen2.tokenize import generate_tokens
from Crypto.Cipher import AES 
from base64 import * 
import os
from tkinter import Tk
from tkinter.filedialog import askopenfile, askopenfilename as openfile     
from cryptography.fernet import Fernet
Tk().withdraw()
PLAIN = os.path.abspath('FILE/')
ENCRYPTED = os.path.abspath('FILE/ENCRYPTED/')
DECRYPTED = os.path.abspath('FILE/DECRYPTED/')

key = Fernet.generate_key()
key = key.encode('utf-8')

def encrypt( filename , key):
    with open (filename , "rb") as file:
        data =  file.read()
        cipher = AES.new(key,AES.MODE_CBC)
        text =cipher.encrypt(data,AES.block_size)
        iv = b64encode(cipher.iv).decode('UTF-8')
        text = b64encode(text).decode('UTF-8')
        write = iv + text 
        print(AES.block_size)
    file.close()
    with open(filename+'.enc','w') as encrypted : 
        data.write(text)
    data.close()
    print("ca marche pelo ")


def delete(filename):
    os.remove(filename)

def encryption():
    print('Choose ur file')
    a = input('press enter ton continue')
    filename= askopenfile()
    encrypt(filename,key)

encryption()
print('test de con')