func sumOfUnique(nums []int) int {
    counts := make(map[int]int, 0)

    for _, num := range nums {
        counts[num] += 1
    }

    sum := 0
    for key, val := range counts {
        if val == 1 {
            sum += key
        }
    }
    return sum
}