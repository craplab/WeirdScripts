# Self Printing Program

> A quine is a computer program which takes no input and produces a copy of its own source code as its only output. The standard terms for these programs in the computability theory and computer science literature are "self-replicating programs", "self-reproducing programs", and "self-copying programs". [wikipedia](https://en.wikipedia.org/wiki/Quine_(computing)#:~:text=A%20quine%20is%20a%20computer,%22self%2Dcopying%20programs%22.)


### valid Quine program

The program above takes no input and the output is exactly the source code of the program!

given code example prints itself, Run below command
```
$ go run self_printing_prog.go
```

You will get the output as below
```
package main

func main() {
        b:=string(96);
        print(a,b,a,b)
}

var a = `package main

func main() {
        b:=string(96);
        print(a,b,a,b)
}

var a = `
```
