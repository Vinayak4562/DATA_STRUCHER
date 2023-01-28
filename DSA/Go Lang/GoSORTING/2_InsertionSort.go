package main

import "fmt"

// insertion sort perform n-1 Steps
func InsertionSort(A []int) {

	for i := 1; i < len(A); i++ { //Use for iterate an Array
		Cvalue := A[i] //Current Value is used for comparing and Swapping perpose
		position := i  //Used to  comparing the ele with i th index
		for position > 0 && A[position-1] > Cvalue {
			A[position] = A[position-1] // to change the position index
			position = position - 1     // to change the position
		}
		A[position] = Cvalue // here wi will swap the
	}

}

func main() {
	A := []int{3, 5, 8, 9, 6, 2}
	fmt.Println("Original Arraay: ", A)
	InsertionSort(A)
	fmt.Println("Sorted Arraay: ", A)
}
