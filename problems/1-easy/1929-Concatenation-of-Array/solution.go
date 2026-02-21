func getConcatenation(nums []int) []int {
    n := len(nums)
    ans := make([]int, 2*n)
    for i, val := range nums {
        ans[i] = val
        ans[i+n] = val
    }
    return ans
}