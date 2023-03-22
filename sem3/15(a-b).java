import java.util.Scanner;
class Main
{
	public static void main (String[]args){
	Scanner read = new Scanner (System.in);
    int a[] = new int [50];
    int i, min=9999 , max= -9999,n;
    System.out.print("Enter the value of array: ");
    n = read.nextInt();
    System.out.print("Enter the value of array: ");
    for(i=0;i<n;i++)
    {
        a[i] = read.nextInt();
    }
    for(i=0;i<n;i++)
    {
        if(a[i]>max)
        {
        max = a[i];
        }
        if(a[i]<min)
        {
        min = a[i];
        }
    }
    System.out.println("maximum value of array: " +max);
    System.out.println("minimum value of array: " +min);
}
}





import java.util.Scanner;
class Main
{
	public static void main (String[]args){
	Scanner read = new Scanner (System.in);
    int a[] = new int [50];
    int i,n,search;
    System.out.print("Enter the limit of array: ");
    n = read.nextInt();
    for(i=0;i<n;i++)
    {
        System.out.print("Enter " + i+1 + " st value of array: ");
        a[i] = read.nextInt();
    }
    System.out.println();
    System.out.print("Enter the Element of search: ");
    search = read.nextInt();
    
    for(i=0;i<n;i++){
        if(search==a[i]){
            System.out.println("your Entered " +search+ " is at " + i+1 + "nd position in array: ");
            break;
        }
    }
	if(search!=a[i]){
		System.out.println( +search+ " Not found");
}   
}
}


