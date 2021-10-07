# Self Printing Program

> A quine is a computer program which takes no input and produces a copy of its own source code as its only output. The standard terms for these programs in the computability theory and computer science literature are "self-replicating programs", "self-reproducing programs", and "self-copying programs". 

[wikipedia](https://en.wikipedia.org/wiki/Quine_(computing)#:~:text=A%20quine%20is%20a%20computer,%22self%2Dcopying%20programs%22.)



### valid Quine program in Ruby

The program in [quine.rb](quine.rb) takes no input and the output is exactly the source code of the program!

Run below command:
```
$ ruby quine.rb
```

You will get the output as below
```rb
src = "\nputs \"src = \" + src.inspect + src"
puts "src = " + src.inspect + src
```