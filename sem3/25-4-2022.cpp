Query 1 : Single level control break.

#include <iostream>
using namespace std;

int main ()
{
    int i, j;
    cout << "Enter any value : ";
    cin >> i;
    for (i = 1 ; i <= 3 ; i++ )
    {
        cout << " i= " << i << endl;
        for (j=1 ; j <= 3 ; j++)
        {
            cout << " j= " << j << endl;
            if (i % 2 == 0)
            {
                break;
            }
        }
    }
	return 0;
}


import java.util.Scanner;
class Main
{
    public static void main (String [] args)
    {
        Scanner x = new Scanner(System.in);
        int i, j;
        System.out.print("Enter any number : ");
        i = x.nextInt();
        for (i = 1 ; i <= 3 ; i++ )
        {
            System.out.print( " i= " + i + "\n" );
            for (j=1 ; j <= 3 ; j++)
            {
                 System.out.print( " j= " + j + "\n" );
                if (i % 2 == 0)
                {
                    break;
                    
                }
            }
        }
    }
}


Query 2 : Java Nestedloop. Multi level control break.


import java.util.Scanner;
class Main
{
    public static void main (String [] args)
    {
        Scanner x = new Scanner(System.in);
        int i, j;
        System.out.print("Enter any number : ");
        i = x.nextInt();
        NestedLoop:
            for (i = 1 ; i <= 3 ; i++ )
            {
                System.out.print( " i= " + i + "\n" );
                for (j=1 ; j <= 3 ; j++)
                {
                    System.out.print( " j= " + j + "\n" );
                    if (i % 2 == 0)
                    {
                        break NestedLoop;
                    
                    }
                }
           }
    }
}


Query 3 : Multi level control break in C++ goto loop.

#include <iostream>
using namespace std;

int main ()
{
    int i, j;
    cout << "Enter any value : ";
    cin >> i;
    for (i = 1 ; i <= 3 ; i++ )
    {
        cout << " i= " << i << endl;
        for (j=1 ; j <= 3 ; j++)
        {
            cout << " j= " << j << endl;
            if (i % 2 == 0)
            {
                goto outside;
            }
        }
        outside:
        {
            cout << "rrrrrrrrrrrrrrrrrrrr";
        }
    }
	return 0;
}


Query 4 : 

#include <iostream>
using namespace std;

int main()
{
    int i, j, k, n=1;
    char c = 'A';
    cout << "Enter any value : ";
    cin >> i;
    for( i = 1 ; i <= 5 ; i++)
    {
        if ( i % 2 != 0 )
        {
            for( j=1 ; j <= i ; j++)
            {
                cout << n;
            }
            n=n + 2;
        }
        else
        {   
            for(k=1;k<=i;k++)
            {
                cout<<c;
            }
            c++;
        }
        cout<<endl;
    }
	return 0;
}

Query 5 : Regular trinagle.


#include <iostream>
using namespace std;

int main()
{
    int i, j, k, n=1;
    char c = 'A';
    cout << "Enter any value : ";
    cin >> i;
    for( i = 1 ; i <= 4 ; i++)
    {
        for( j = 4 ; j > i ; j--)
        {
           cout << " ";
        }
        for(k=1;k<=i;k++)
        {
        cout<< n << " " ;
        n++;
        }
        cout<<endl;
    }
    return 0;
}