func subsets(nums []int) [][]int {
    res := [][]int{{}}
    path := []int{}
    for i, _ := range nums {
        dfs(nums, i, &path, &res)
    }
    return res
}

func dfs(nums []int, index int, path *[]int, res *[][]int) {
    *path = append(*path, nums[index])
    copy := append([]int{}, *path...)
    *res = append(*res, copy)

    for i := index + 1; i < len(nums); i++ {
        dfs(nums, i, path, res)
    }
    *path = (*path)[:len(*path)-1]
}