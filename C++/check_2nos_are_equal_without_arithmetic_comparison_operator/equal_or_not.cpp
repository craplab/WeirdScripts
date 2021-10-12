#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cout << "Enter two numbers ";
    cin >> a >> b;
    
   if (!(a ^ b))
      cout << "a is equal to b ";
   else
      cout << "a is not equal to b ";

   return 0;
}