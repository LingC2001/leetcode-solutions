func subsets(nums []int) [][]int {
    res := [][]int{}
    path := []int{}
    dfs(nums, 0, &path, &res)
    return res
}

func dfs(nums []int, start int, path *[]int, res *[][]int) {
    copy := append([]int{}, *path...)
    *res = append(*res, copy)

    for i := start; i < len(nums); i++ {
        *path = append(*path, nums[i])
        dfs(nums, i+1, path, res)
        *path = (*path)[:len(*path)-1]
    }
}