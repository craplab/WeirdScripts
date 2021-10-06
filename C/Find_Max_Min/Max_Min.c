// C program to find maximum and minimum of
// two numbers without using loop and any
// condition.
#include<stdlib.h>
#include<stdio.h>

int main ()
{
   int a = 15, b = 20;
   printf("input A:");
   scanf("%d",&a);

   printf("input B:");
   scanf("%d",&b);
   printf("max = %d\n", ((a + b) + abs(a - b)) / 2);
   printf("min = %d", ((a + b) - abs(a - b)) / 2);
   return 0;
}
