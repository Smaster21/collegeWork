\\ pract 20 java\\
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




\\ pract 21 java \\
import java.util.Scanner;
class Main
{
    public static void main(String[]args){
    Scanner read = new Scanner (System.in);
    String a,vow = "aeiouAEIOU";
    int i,j,n,slen,vlen,vowels=0;
    System.out.print("Enter any String : ");
    a =read.nextLine();
    slen = a.length();
    vlen = vow.length();
    for (i=0 ; i<slen ; i++){
        for(j=0 ; j<vlen ; j++){
            if(a.charAt(i)==vow.charAt(j)){
                vowels++;
            }
        }
    }
    System.out.println("No of vowels in String : " +vowels);
}
}




\\ pract 22 java \\
import java.util.Scanner;
class Main
{
     public static void main(String[] args){
        Scanner read = new Scanner (System.in);
        String a,b = "";
        int i,j;
        System.out.print("Enter ant string : ");
        a = read.nextLine();
        int n = a.length();
        for ( i = 0; i < n ; i++){
            for ( j = 0; j < i ; j++){
                if (a.charAt(i) == a.charAt(j)){
                    break;
                }
            }
            if (i==j){
                b = b + a.charAt(i);
            }
            }
		System.out.println("Removing duplicate Character : " +b);
	}
}




\\pract 23 java\\
import java.util.Scanner;
class Main{
    static int sum(int n)
    {
        int sum = 0,i;
        for (i = 1; i <= n; i++)
            sum = sum + i;
        return sum;
    }
    public static void main(String[]args)
    {
        Scanner read = new Scanner (System.in);
        int n;
        System.out.print("Enter any value : ");
        n = read.nextInt();	
        System.out.println("Sum of first " + n + " number is : " +sum(n));
    }
}
 
 

\\pract 24 java\\ 
import java.util.Scanner;
class Main
{
    static int sum(int n){
     if (n==0){
         return 1;
        }
            return n*sum(n-1);
        }
        public static void main(String[]args){
        Scanner read = new Scanner (System.in);
        int n;           
        System.out.print("Enter the value : ");
        n = read.nextInt();
        System.out.println("The factorial of " + n + " is : " +sum(n));
    }
}



\\pract 25 java\\
import java.util.Scanner;
enum day {Sunday ,Monday ,Tuesday ,Wednesday ,Thursday ,Friday ,Saturday}
class Main {
   public static void main(String[] args) {
      System.out.println(day.Friday);
   }
}
