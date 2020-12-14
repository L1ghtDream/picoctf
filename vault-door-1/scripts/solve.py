
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