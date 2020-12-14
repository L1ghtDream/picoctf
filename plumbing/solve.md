```
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 14291.
```

If we just netcat to the given adress we got a long output and because it is on a terminal 

```
nc jupiter.challenges.picoctf.org 14291 > out.txt
```


I could not **CTRL+F** thru it so I saved it in a file and then **CTRL+F** thru it and here is the flag **picoCTF{digital_plumb3r_ea8bfec7}**