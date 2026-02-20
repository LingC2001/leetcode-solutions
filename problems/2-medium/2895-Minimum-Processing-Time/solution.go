import "slices"
func minProcessingTime(processorTime []int, tasks []int) int {
    slices.Sort(processorTime)
    slices.Sort(tasks)
    slices.Reverse(tasks)

    for i, val := range processorTime {
        for j := 0; j < 4; j++ {
            tasks[i*4 + j] += val
        }
    }
    return slices.Max(tasks)
}