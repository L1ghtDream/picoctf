```
'Suspicious' is written all over this disk image. Download suspicious.dd.sda1
```

First thing that I tryed was simply editing the file to check the meta data maybe there is the flag but I got not luck.
Then I viwing the hex with **Binary ninja** but still nothing
After I tryed mounting the image to my linux machinine and dd the files and I got the files 

```
sudo dd if=suspicious.dd.sda1 skip=2098176 count=128 iflag=skip_bytes,count_bytes of=slice
xxd slice
```

Here is the flag **picoCTF{b3_5t111_mL|_<3_f5290af6}**