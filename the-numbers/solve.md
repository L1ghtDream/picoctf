```
The numbers... what do they mean?
```

![img](https://raw.githubusercontent.com/L1ghtDream/picoctf/master/the-numbers/files/the_numbers.png?raw=true)


We are provided wiht a **.png** file and it contains a flag like format with **[...]{[...]}**
Here are the numbers 

```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14}
```

Upon closer inspection because I knew that fact that the flag needs to start with **PICOCTF{[...])**
so it's clear that the sequance **16 9 3 15 3 20 6** is corespondent to **PICOCTF**. It seems that is just the alphabent.
So I made a little python script:

```
code = input("> ")

print(code)
codes = code.split(" ")
print(codes)

flag = ""

for i in range(0, len(codes)):
    flag = flag + chr(int(codes[i]) + 64)

print(flag + "\n")
```

and we got **PICOCTFTHENUMBERSMASON**. If we add the **{** and the **}** we got **PICOCTF{THENUMBERSMASON}**
