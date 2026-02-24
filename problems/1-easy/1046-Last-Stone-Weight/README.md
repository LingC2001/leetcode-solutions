Use a max heap for retrieving the maximum in log(n)
heapify is O(n)
therefore total time complexity is O(nlog(n))

In Golang, the heap package in standard library provides a interface to implement.

E.g.
```go
import "container/heap"

// An IntHeap is a min-heap of ints.
type IntHeap []int
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
```
You must define the type and implement the 5 methods.

Note when Popping and Pushing, you must use the heap interface methods.

Like so:
```go
my_int_slice := []int{1,2,3}
h := (*IntHeap)(&my_int_slice)
heap.Init(h)
heap.Pop(h)
heap.Push(h, val)
```
Note that h must be the reference/pointer to the IntHeap
