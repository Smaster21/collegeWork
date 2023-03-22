#include<iostream>
using namespace std;
int main() 
{
	char op;
	double num1,num2;
	cout<<"Enter the operator(+,-,*,/):";
	cin>>op;
	cout<<"Enter num 1 : ";
	cin>>num1;
	cout<<"Enter num 2 : ";
	cin>>num2;
	switch(op)
	{
		
		case '+':
			cout<<"Addition of "<< num1 << " and " << num2 << " is : "<<num1+num2;
			break;
		case '-':
		    cout<<"Substraction of " << num1 << " and " << num2 << " is : "<<num1-num2;
		    break;
		case '*':
		    cout<<"Multiplication of " << num1 << " and " << num2 << " is : "<<num1*num2;
		    break;
		case '/':
		    cout<<"Division of " << num1 << " and " << num2 << " is : "<<num1/num2;
		    break;
	}
	return 0;
}
