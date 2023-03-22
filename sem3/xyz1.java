import java.util.Scanner;
class Main
{
    public static void main(String[]args){
        Scanner read = new Scanner (System.in);
        String a,b = "";
        int i, j = 0;
        char t;
        System.out.print("Enter your String : ");
        a = read.nextLine();
        int n = a.length();
        for ( i = n - 1 ; i >= 0 ; i-- )
        {
            t = a.charAt(i);
            b = b+t;
        }
        System.out.println(b+ "\n");
    }
}
