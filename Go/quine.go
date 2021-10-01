package main

import "fmt"

func main() {
	code := `package main
import "fmt"
func main() {
	code := 
	fmt.Print(code[:51] + "\u0060" + code + "\u0060" + code[51:])
}
`
	fmt.Print(code[:51] + "\u0060" + code + "\u0060" + code[51:])
}
