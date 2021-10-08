## Javascript Inferred Type

- The + operator can be binary or unary, in our case we have both,and just for the precedence unary plus is executed first.

- **Unary plus** - Only one value is required to produce result, it convert the value into a number.
- **Binary plus** - Two values are required to produce a result, produces the sum of numeric operands or string concatenation.

&emsp;

- In the example.js, 

&emsp; the input is: `"b" + "a" + + "a" + "a"` 

&emsp; is interpreted as: `"b" + "a" + (+"a") + "a"`

&emsp; ("a") is interpreted as numeric because of the starting +, but "a" cannot be converted to a Number, so the value of "a" is NaN: `"b" + "a" + NaN + "a"` 

&emsp; NaN is converted to a String during concatenation: `"b" + "a" + "NaN" + "a"`

&emsp; and the output will be: `baNaNa`