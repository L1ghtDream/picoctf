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
