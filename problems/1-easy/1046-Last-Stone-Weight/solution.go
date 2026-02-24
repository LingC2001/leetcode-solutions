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

func lastStoneWeight(stones []int) int {
    my_heap := (*IntHeap)(&stones)
    heap.Init(my_heap)
    
    for my_heap.Len() > 1 {
        y := heap.Pop(my_heap).(int)
        x := heap.Pop(my_heap).(int)
        if y != x {
            heap.Push(my_heap, y-x)
        }
    }
    if my_heap.Len() == 1 {
        return heap.Pop(my_heap).(int)
    }

    return 0
}