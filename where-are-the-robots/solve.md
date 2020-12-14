```
Can you find the robots? https://jupiter.challenges.picoctf.org/problem/60915/ (link) or http://jupiter.challenges.picoctf.org:60915
```

If we enter the website we see a basic website with some text and no inputs. So lets open the inspect elemnts. Nothing on here. The chall is named **where are the robots** so lets go to **/robots(.txt .py .js)** so lets try them
And it seams like the **.txt is working**
And we go
```
User-agent: *
Disallow: /8028f.html
```
So lets go now to **/8028f.html** and here is the flag **picoCTF{ca1cu1at1ng_Mach1n3s_8028f}**