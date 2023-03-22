 // write a program to generate multiplication table for givennumber.
 
 #include <iostream>
 using namespace std ;
 int main ()
 {
	 int i,n;
	 cout<<"Enter the number to generate multiplication table : ";
	 cin>>n;
	 for (i=1;i<=10;i++)
	 {
		 cout<< n << " * " << i << " = " << n*i << endl;
	 }
	 return 0;
 }
 
 
 
  //write a program to findsum of first n numbers.
  
  #include <iostream>
  using namespace std;
  int main ()
  {
	 float i,n,sum=0;
	 cout<<"Enter the number : ";
	 cin>>n;
	 for (i=1;i<=n;i++)
	 {
		 sum = sum + i;
		 cout<<sum<<endl;
	 }
	     return 0;
  }
  
  
  
  //write a program to print fibbonacci series for n number.
  
   #include <iostream>
 using namespace std ;
 int main ()
 {
    int a=0,b=1,c,i,n;
    cout<<"Enter the number : " ;
    cin>>n;
    cout<< a << endl;
    cout<< b << endl;
    for(i=0 ; i <= n ; i++)
    {
        c = a+b;
        cout<< c << endl;
        a = b;
        b = c;
    }
	     return 0;
 }