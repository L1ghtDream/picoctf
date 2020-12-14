```
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java
```

If we just edit the file in **Notepad++** we get the source code. If we look at the function **checkPassword** we got

```
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
```

if we just copy all check staics we got **d9r5rc43b_43tclHc_m5r34TH52_307e** but we can see that is not a real flag if we take a closer look we can see that we have a **.charAt** so I added all chars to a string in that order with the next python script

```

flagArray = [0 for i in range(32)] 
flag = ""

flagArray[0]  = 'd'
flagArray[29] = '9'
flagArray[4]  = 'r'
flagArray[2]  = '5'
flagArray[23] = 'r'
flagArray[3]  = 'c'
flagArray[17] = '4'
flagArray[1]  = '3'
flagArray[7]  = 'b'
flagArray[10] = '_'
flagArray[5]  = '4'
flagArray[9]  = '3'
flagArray[11] = 't'
flagArray[15] = 'c'
flagArray[8]  = 'l'
flagArray[12] = 'H'
flagArray[20] = 'c'
flagArray[14] = '_'
flagArray[6]  = 'm'
flagArray[24] = '5'
flagArray[18] = 'r'
flagArray[13] = '3'
flagArray[19] = '4'
flagArray[21] = 'T'
flagArray[16] = 'H'
flagArray[27] = '5'
flagArray[30] = '2'
flagArray[25] = '_'
flagArray[22] = '3'
flagArray[28] = '0'
flagArray[26] = '7'
flagArray[31] = 'e'

for i in range(0, len(flagArray)):
    flag = flag + str(flagArray[i])

print(flag)
```

And we got **d35cr4mbl3_tH3_cH4r4cT3r5_75092e** so the flag is **picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}**


