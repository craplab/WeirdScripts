#include <stdio.h>
void printNumber(int count)
{
   printf("%d\n", count );
   count+=1;
   if(count<=10)
      printNumber(count);
}
int main()
{
   printNumber(1);
   return 0;
}