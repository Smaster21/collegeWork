#include <iostream>
using namespace std;

int main ()
{
	double Marks ;
	cout << " Enter the marks : " ;
	cin >> Marks ;
	if (Marks == 12)
	{
		cout << " Congratulation you have passed with D Grades. " ;
	}
	else if ( Marks >= 13  && Marks<= 20)
	{
		cout << " Congratulation you have passed with C Grades. ";
	}
	else if ( Marks >= 21 && Marks<= 25)
	{
		cout << " Congratulation you have passed with B Grades. ";
	}
	else if ( Marks >= 26 && Marks<= 30)
	{
		cout << " Congratulation you have passed with A Grades. ";
	}
	else if ( Marks < 12)
	{
		cout << " Alert! You are failed and you have to give makeup test to clear the Subject.";
	}
	else if ( Marks > 30)
	{
		cout << " You have Entered invalid Marks . ";
	}
	return 0;
}