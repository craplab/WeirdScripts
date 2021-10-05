// C++ Program to swap two numbers  without using temporary variable

#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int a = 11, b = 6;
 
    // Code to swap 'a' and 'b'
    a = a + b; 
    b = a - b; 
    a = a - b; 
    cout << "After Swapping: a =" << a << ", b=" << b;
}