import base64

code = input("> ")

print(base64.b64decode(bytes(code, 'utf-8')))
print("\n")