#include<iostream>
using namespace std;
int main ()
{
	int i;
	for (i=1;i<=10;i++)
	{
		cout<<i<<endl;
	
	}
	cout<<"end";
	return 0;
}


#include<iostream>
using namespace std;
int main ()
{
	int i;
	for (i=10;i>=1;i--)
	{
		cout<<i<<endl;
	
	}
	cout<<"end";
	return 0;
}



#include<iostream>
using namespace std;
int main ()
{
	int i;
	for (i=16; i<=30; i=i+2)
	{
		cout<<i<<endl;
	}
	cout<<"end";
	return 0;
}
 
 
 //print number which are divisible by 7 for range 20 to 50.

#include<iostream>
using namespace std;
int main ()
{
	int i;
	for (i=20; i<=50; i++)
	{
	    if (i%7 == 0)
	    {
		cout<<i<<endl;
	    }
	}
	cout<<"end";
	return 0;
}



 //print number which are divisible by 5 or 3 for range 51 to 80.

#include<iostream>
using namespace std;
int main ()
{
	int i;
	for (i=80; i>=51; i--)
	{
	    if (i % 5 == 0 && i % 3 ==0 )
	    {
		cout<<i<<endl;
	    }
	}
	cout<<"end";
	return 0;
}

 // write a program to find factorial value for given number.
 
 #include<iostream>
using namespace std;
int main ()
{
	double i,n,Fact=1;
	cout<<"Enter the num : ";
	cin>>n;
	for (i=n; i>=1; i--)
	{
	    Fact = Fact * i;
	}
	cout<<"The factorial of n is : "<< Fact << endl << "end";
	return 0;
}




