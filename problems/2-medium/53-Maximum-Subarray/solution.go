func maxSubArray(nums []int) int {
    sum := nums[0]
    max_sum := sum
    for i := 1; i < len(nums); i++ {
        if sum < 0 {
            sum = nums[i]
        } else {
            sum += nums[i]
        }
        
        if sum > max_sum {
            max_sum = sum
        }
    }

    return max_sum
}
