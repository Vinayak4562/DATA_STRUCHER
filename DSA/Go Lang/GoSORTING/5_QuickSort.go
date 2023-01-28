package main

import "fmt"

func partition(A []int, low, high int) int {
	pivot := A[low]
	i := low
	j := high

	for i < j {
		for A[i] <= pivot && i < high {
			i++
		}
		for A[j] > pivot && j > low {
			j--
		}

		if i < j {
			temp := A[i]
			A[i] = A[j]
			A[j] = temp
		}
	}
	A[low] = A[j]
	A[j] = pivot

	return j
}
func quickSort(A []int, low, high int) {
	if low < high {
		pivot := partition(A, low, high)
		quickSort(A, low, pivot)
		quickSort(A, pivot+1, high)
	}
}

func main() {
	A := []int{15, 3, 12, 6, -9, 9, 0}

	fmt.Println("Before Sorting: ", A)
	quickSort(A, 0, len(A)-1)
	fmt.Println("After Sorting: ", A)

}

// Time Complexity
// Best complexity: n*log(n)
// Average complexity: n*log(n)
// Worst complexity: n^2
