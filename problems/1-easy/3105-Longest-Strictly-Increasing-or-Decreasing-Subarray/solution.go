func longestMonotonicSubarray(nums []int) int {
    max_size := 1
    inc_size := 1
    dec_size := 1

    for i := 1; i < len(nums); i++ {
        if nums[i] > nums[i-1] {
            inc_size += 1
            dec_size = 1
        } else if nums[i] < nums[i-1] {
            dec_size += 1
            inc_size = 1
        } else {
            inc_size = 1
            dec_size = 1
        }

        max_size = max(max_size, inc_size, dec_size)
    }
    return max_size