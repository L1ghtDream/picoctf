```
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: VaultDoorTraining.java
```

Just for sanity check I tryed editing it with **Notepad++** and to my surprize this is not encrypted or compiled or anything like that this is just a java script. And we can just see the password was just laying on there **w4rm1ng_Up_w1tH_jAv4_be8d9806f18**.
Not even that but even the comments told us that 

```
// The password is below. Is it safe to put the password in the source code?
// What if somebody stole our source code? Then they would know what our
// password is. Hmm... I will think of some ways to improve the security
// on the other doors.
//
// -Minion #9567
```

And here is the flag **picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}**