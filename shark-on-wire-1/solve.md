```
We found this packet capture. Recover the flag.
```

Firsh thing that I did was oppeing the file in wireshark and searching for the string **pico** but I did not had any luck because I did not found any flag. But I saw that in some packets the word **pico** or **CTF** or **{** are visble so I may have a path to fallow. And I observed the fact that all the packets sent to **10.0.0.12** with **UDP** are the ones that we need so I constructed the flag by hand and here it is **picoCTF{StaT31355_636f6e6e}**