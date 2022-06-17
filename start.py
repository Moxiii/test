import codecs 
import os
import sys 
import hashlib
import pyexpat.errors 
from base64 import *
from fileinput import filename
from Crypto.Cipher import AES 
from tkinter import Tk
from tkinter.filedialog import askopenfile, askopenfilename as openfile     
from cryptography.fernet import Fernet
import pandas as pd
import shutil
Tk().withdraw()
PLAIN = os.path.abspath('FILE/test.txt')
ENCRYPTED = os.path.abspath('FILE/ENCRYPTED/')
DECRYPTED = os.path.abspath('FILE/DECRYPTED/')

key = Fernet.generate_key()
key = b64encode(key)

def __init__(self,filename):
    with open (filename,"r") as file :
        CSV = pd.read_csv(file)
        codecs.encode(CSV,encoding='utf-8')
    
def encrypt( filename , key):
    codecs.encode(filename,encoding='utf-8')
    with open (filename , "r") as file:
        data =  file.read()
        cipher = AES.new(key,AES.MODE_CBC)
        text =cipher.encrypt(data,AES.block_size)
        iv = b64encode(cipher.iv).decode('UTF-8')
        text = b64encode(text).decode('UTF-8')
        write = iv + text 
        print(AES.block_size)
        CSV = pd.read_csv(file)
    file.close()
    with open(filename+'.enc','w') as encrypted : 
        data.write(text)
        CSV = pd.read_csv(file)
    data.close()
    print("ca marche pelo ")

    

def delete(filename):
    os.remove(filename)

def encryption(filename):

    print('Choose ur file')
    a = input('press enter ton continue')
    filename= askopenfile()
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
    codecs.encode(filename,encoding='UTF-8')
    encrypt(filename,key)
def plain_to_enc():
    shutil.copy(PLAIN,ENCRYPTED)

def enc_to_dec():
    shutil.move(ENCRYPTED,DECRYPTED)
encryption('PLAIN/test.txt')
print("worked")