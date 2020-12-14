```
Can you convert the number 42 (base 10) to binary (base 2)?
```

We can see that this is a preaty basic chall so I just wrote a script in **python** just to have it.

```
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')
	

number = int(input("> "))

decimalToBinary(number)
print("\n")
```

And here is the flag **picoCTF{101010}**