func getSumAbsoluteDifferences(nums []int) []int {
    n := len(nums)
    res := make([]int, n)
    sum := 0
    for _, val := range nums {
        sum += val
    }
    res[0] = sum - n*nums[0]

    for i := 1; i < n; i++ {
        diff := nums[i] - nums[i-1]
        res[i] = i*diff + res[i-1] - (n-i)*diff
    }
    return res
}