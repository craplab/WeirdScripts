#include <iostream>
using namespace std;
int main()
{
    int n1, n2;
    cout<<"Enter two numbers";
    cin>>n1>>n2;
    if (n2 > 0) {
        while (n2 > 0) {
            n1++;
            n2--;
        }
    }
    if (n2 < 0) { // when 'b' is negative
        while (n2 < 0) {
            n1--;
            n2++;
        }
    }
    cout<<"Sum = "<< n1;
    return 0;
}
