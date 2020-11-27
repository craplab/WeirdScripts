#include <stdio.h>

// prototypes
int subtract(int x, int y);
int sum(int x, int y);
int Add(int x, int y);

/*  Checks if the integers passed are -ve, +ve
    and calls appropriate func to add them  */

int Add(int x, int y){
    if((x > 0 && y > 0)||(x < 0 && y < 0))
        return sum(x, y);
    else if (x > 0 && y < 0)
        return subtract(x, y*(-1));
    else
        return subtract(y, x*(-1));    
}

/*  Uses bitwise adder logic having carry  */
int sum(int x, int y){
    while (y != 0){ 
        int c = x & y;   
        x = x ^ y;      
        y = c << 1; 
    } 
    return x; 
} 

/*  Uses bitwise subtracted logic having borrow */
int subtract(int x, int y){
    while (y != 0){ 
        int b = (~x) & y; 
        x = x ^ y; 
        y = b << 1; 
    } 
    return x; 
}

// Driver function
int main(){
    printf(" 4 +   5  =  %d\n", Add(4,5));
    printf(" 4 + (-5) = %d\n", Add(4,-5));
    printf("-4 +   5  =  %d\n", Add(-4,5));
    printf("-4 + (-5) = %d\n", Add(-4,-5));
}
