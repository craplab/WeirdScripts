# Self Printing Program

> A quine is a computer program which takes no input and produces a copy of its own source code as its only output. The standard terms for these programs in the computability theory and computer science literature are "self-replicating programs", "self-reproducing programs", and "self-copying programs". [wikipedia](https://en.wikipedia.org/wiki/Quine_(computing)#:~:text=A%20quine%20is%20a%20computer,%22self%2Dcopying%20programs%22.)

### invalid Quine program

```python
print(open(__file__).read())
```
The program above is not a Quine program because the program reads its source code as file, thus making it using itself as input. 

### valid Quine program

```python
variable = 'print("variable = " + repr(variable) + "\\neval(variable)")'
eval(variable)
```
The program above takes no input and the output is exactly the source code of the program!

[source code and more examples](https://towardsdatascience.com/how-to-write-your-first-quine-program-947f2b7e4a6f)
