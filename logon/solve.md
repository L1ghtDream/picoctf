```
The factory is hiding things from all of its users. Can you login as logon and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/13594/ (link) or http://jupiter.challenges.picoctf.org:13594
```

If we go to the webise we are greated with some login site  and we conect with some random credentials we can see that we are not allowed to get the flag. If we look at the networking tab we can see that the cookie is sending if we are admin or not. So I opened burp done the same thing and modifyed the payload to say that I am the admin and we got the flag **picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}**