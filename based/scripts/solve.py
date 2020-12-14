from pwn import *
from ptrlib import *
import numpy as np

def getOct(s):
    octdata = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #           0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25

    idOct = s

    if(s>=150):
        idOct = idOct - 2
    if(s>=160):
        idOct = idOct - 2
    if(s>=170):
        idOct = idOct - 2
        
    return octdata[idOct-141]





sock = Socket('jupiter.challenges.picoctf.org', 15130)

#------------------Level 1------------------
resp = sock.recv().decode("utf-8")

datas = resp.split(" ")
save = 0;
decode = ""

for i in range(0, len(datas)):
    if(datas[i] == "as"):
        save = 0
        break
        
    if(save == 1):
        decode = decode + chr(int(str(datas[i]), 2))
        
    if(datas[i] == "the"):
        save = 1
        
sock.sendline(decode)

#------------------Level 2------------------

resp = sock.recv().decode("utf-8")

datas = resp.split(" ")
save = 0;
decode = ""

for i in range(0, len(datas)):
    if(datas[i] == "as"):
        save = 0
        break
        
    if(save == 1):
        decode = decode + getOct(int(datas[i]))
        
    if(datas[i] == ""):
        save = 1
        
        
sock.sendline(decode)

#------------------Level 3------------------


resp = sock.recv().decode("utf-8")

datas = resp.split(" ")
save = 0;
decode = ""

for i in range(0, len(datas)):
    if(datas[i] == "as"):
        save = 0
        break
        
    if(save == 1):
        decode = bytearray.fromhex(datas[i]).decode()
        
    if(datas[i] == "the"):
        save = 1
        

sock.sendline(decode)

#------------------FLAG------------------


resp = sock.recv().decode("utf-8")
print(resp)



sock.close()

