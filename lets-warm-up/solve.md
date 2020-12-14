```
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
```

Here I made a python script to decode it

```
code = input("> ")

print(bytearray.fromhex(code).decode())
print("\n")
```

The output is **p** and so the flag is **picoCTF{p}**