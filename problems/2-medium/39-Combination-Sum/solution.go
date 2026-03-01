func combinationSum(candidates []int, target int) [][]int {
    res := [][]int{}
    path := []int{}
    backtrack(candidates, target, 0, &path, 0, &res)
    return res
}

func backtrack(candidates []int, target int, sum int, path *[]int, index int, res *[][]int) {
    if sum == target {
        copy := append([]int{}, *path...)
        *res = append(*res, copy)
    } else if sum > target {
        return
    }

    for i := index; i < len(candidates); i++ {
        *path = append(*path, candidates[i])
        backtrack(candidates, target, sum+candidates[i], path, i, res)
        *path = (*path)[:len(*path)-1]
    }
}