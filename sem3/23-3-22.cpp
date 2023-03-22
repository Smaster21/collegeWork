 // print 1-10 using while loop.

#include < iostream >
using namespace std ;
int main ()
{
	int i=1;
	while(i<=10)
	{
		cout<<i<<endl;
		i++
	}
	return 0;
}


 // print 1-10 using do-while loop.
 
 #include <iostream>
using namespace std ;
int main ()
{
	int i=1;
	do
	{
		cout<<i<<endl;
		i++;
	}
	    while(i<=10);
	return 0;
}


 // print prime number or not using for loop. 
 
#include <iostream>
using namespace std ;
int main ()
{
	int a,c,count=0; // (count/flag  is just a variable.)
	cout<<"Enter any number : ";
	cin>>c;
		for(a=2; a<c ; ++a)
      {
         if(c%a == 0)
         {
            count++;
            break;
         }
      }
      
      if(count==0)
         cout<<("This number is a Prime Number.");
      else
         cout<<("This number is not a Prime Number.");
         return 0;
}


 // write a program to find prime number from given range.
 
 #include <iostream>
using namespace std ;
int main ()
{
	int a,c,count=0,j;
	cout<<"Enter any number : ";
	cin>>c;
		for(a=1; a<c ; a++)
      {
          for (j=2 ; j<a ; j++)
         {
            count = 0;
            if(a%j==0)
            {
            count=1;    
            break;
            }
         }
    }
      
      if(count==0)
         cout<<("This number is a Prime Number.");
      else
         cout<<("This number is not a Prime Number.");
         return 0;
}

