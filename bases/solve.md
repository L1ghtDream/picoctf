```
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.
```

This seems to be a **base64** encoding so I made a **python** script to decode it

```
import base64

code = input("> ")

print(base64.b64decode(bytes(code, 'utf-8')))
print("\n")
```

And we got **b'l3arn_th3_r0p35'** so the falg is **picoCTF{l3arn_th3_r0p35}**