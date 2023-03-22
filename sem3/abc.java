import java.util.Scanner;
class abc
{
	public static void main (String[]args)
	{
		int a[] = new int [50];
		Scanner read = new Scanner (System.in);
		int i,j,n,temp;
		System.out.print("Enter the num you like : ");
		n = read.nextInt();
		for(i=0;i<n;i++){
		a[i] = read.nextInt();
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			if(a[i] < a[j])
		{
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
		}
		}
		System.out.println("The element sorting after element change : ");
		for(i=0;i<n;i++){
			System.out.print(a[i]+"\n");
		}
		}
}
		
