// to take input from user for string getchar function//
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char a[20];
    char c;
    int i = 0;
    do
    {
        c = getchar();
        a[i] = c;
        i++;
    } 
    while ( c != '\n' );
    cout << a;
    return 0;
}




// write a program to print string using putchar function//
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    char a[20];
    cin >> a;
    int i;
    for ( i = 0 ; a[i] != '\0' ; i++ )
    {
        putchar(a[i]);
    }
    return 0;
}




// write a program to take input and print enterednstring using gets and puts function//
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    char a[20];
    cout << "Enter your String : ";
    gets(a);
    cout << "Enter string is : ";
    puts(a);
    return 0;
}






