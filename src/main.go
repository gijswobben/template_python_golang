package main

import (
	"C"
	"fmt"
)

//export Hello
func Hello() {
	fmt.Println("Hi there")
}

//export Greet
func Greet(name string) int {
	fmt.Printf("Hello %v\n", name)
	return 0
}

//export Factorial
func Factorial(n uint64) (result uint64) {
	if n > 0 {
		result = n * Factorial(n-1)
		return result
	}
	return 1
}

func main() {}
