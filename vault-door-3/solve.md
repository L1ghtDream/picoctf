```
This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java
```

If we edit the file we can see 

```
public boolean checkPassword(String password) {
	if (password.length() != 32) {
		return false;
	}
	char[] buffer = new char[32];
	int i;
	for (i=0; i<8; i++) {
		buffer[i] = password.charAt(i);
	}
	for (; i<16; i++) {
		buffer[i] = password.charAt(23-i);
	}
	for (; i<32; i+=2) {
		buffer[i] = password.charAt(46-i);
	}
	for (i=31; i>=17; i-=2) {
		buffer[i] = password.charAt(i);
	}
	String s = new String(buffer);
	return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
}
```

here we got multiple things. First we got a scrumble algorithm and the correct output of that scramble algorithm so lets back engineer that.

```
public class main {
    public static void main(String[] args) {

        String buffer = "jU5t_a_sna_3lpm18g947_u_4_m9r54f";
        char[] password = new char[32];

        int i;

        for (i=0; i<8; i++) 
            password[i] = buffer.charAt(i);

        for (; i<16; i++)
            password[23-i] = buffer.charAt(i);

        for (; i<32; i+=2)
            password[46-i] = buffer.charAt(i);

        for (i=31; i>=17; i-=2)
            password[i] = buffer.charAt(i);

        System.out.println(new String(password));

    }
}

```

And here is the flag **picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}**

