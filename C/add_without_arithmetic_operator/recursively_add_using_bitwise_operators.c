/**
 * @file
 * @author (Randy Kwalar)[https://github.com/RandyKdev]
 * 
 * @brief This program recursively adds 2 integers without using addition operators
 */

#include <assert.h> /// for the assert function

/**
 * @brief Adds 2 integers `x` and `y`
 * @param x The first integer to add
 * @param y The second integer to add
 * @returns The sum of `x` and `y`
 */
int add(int x, int y) {
    // Base case
	if (y == 0) return x;

    // Recursive case

    // carry holds common bits found in x and y
    unsigned carry = x & y; 
 
    // x holds the sum of bits of x and y
    x = x ^ y;
 
    // carry is shifted by one and assigned to y
    y = carry << 1;

    // add is called again for the different values of x and y
    return add(x, y);
}

/**
 * @brief Self-test implementations
 * @returns void
 */
void test() {
    // These are self-test implementations of the program
    assert(add(4, 6) == 10);
    assert(add(-2, 5) == 3);
    assert(add(-5, 3) == -2);
    assert(add(-3, -2) == -5);
    assert(add(-3, 0) == -3);
    assert(add(0, -2) == -2);
}

/**
 * @brief The Main function
 * @returns 0
 */
int main(void) {
    // runs self-test implementations
    test();

    return 0;
}
