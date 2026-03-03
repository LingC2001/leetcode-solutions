func subsetsWithDup(nums []int) [][]int {
    slices.Sort(nums)
    res := [][]int{}
    backtrack(nums, 0, &[]int{}, &res)
    return res
}

func backtrack(nums []int, first int, path *[]int, res *[][]int) {
    pathCopy := make([]int, len(*path))
    copy(pathCopy, *path)
    *res = append(*res, pathCopy)

    for i := first; i < len(nums); i++ {
        if i > first && nums[i] == nums[i-1] {
            continue
        }
        *path = append(*path, nums[i])
        backtrack(nums, i+1, path, res)
        *path = (*path)[:len(*path)-1]
    }
}