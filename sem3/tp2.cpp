#include <iostream>
using namespace std;
int main ()
{
		int a;
		cout<<"Enter the value of a : ";
		cin>>a;
		if (a%2==0)
		{
			goto even;
		}
		else 
		{
			goto odd;
		}
		even:
			cout<<"a is even number."<<endl;
		odd:
			cout<<"a is odd number."<<endl;
		return 0;
}