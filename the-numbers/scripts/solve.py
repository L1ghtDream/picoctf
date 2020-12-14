code = input("> ")

print(code)
codes = code.split(" ")
print(codes)

flag = ""

for i in range(0, len(codes)):
    flag = flag + chr(int(codes[i]) + 64)

print(flag + "\n")