package main

import "fmt"

func selectionsort(A []int) {
	n := len(A)
	for i := 0; i < n-1; i++ { // Used to sort an arry elements
		position := i
		for j := i + 1; j < n; j++ { // Used ti itterate an arry
			if A[position] > A[j] { // to finding an smallest number
				position = j
			}
		}
		A[position], A[i] = A[i], A[position] // Here we will perform Swapping
	}
}

func main() {
	A := []int{7, 2, 5, 6, 1, 3}
	fmt.Println("Original Array: ", A)
	selectionsort(A)
	fmt.Println("Array after sorting: ", A)
}
