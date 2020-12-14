a = [106, 85, 53, 116, 95, 52, 95, 98]
b = ["55", "6e", "43", "68", "5f", "30", "66", "5f"]
c = ['b', 'Y', 't', '3', 's', '_', '8', 'f']
d = ['4', 'a', '6', 'c', 'b', 'f', '3', 'b']

flag = ""

for i in range(0, len(a)):
    flag = flag + chr(a[i])
    
for i in range(0, len(b)):
    flag = flag + bytearray.fromhex(b[i]).decode()

for i in range(0, len(c)):
    flag = flag + c[i]
    
for i in range(0, len(d)):
    flag = flag + d[i]

print(flag)