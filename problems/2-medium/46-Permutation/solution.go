func permute(nums []int) [][]int {
    res := [][]int{}
    path := []int{}
    indexUsed := make(map[int]bool)
    backtrack(nums, &indexUsed, &path, &res)
    return res
}

func backtrack(nums []int, indexUsed *map[int]bool, path *[]int, res *[][]int) {
    if len(*path) == len(nums) {
        copy := append([]int{}, *path...)
        *res = append(*res, copy)
    } 
    
    for i, val := range nums {
        if !(*indexUsed)[i] {
            *path = append(*path, val)
            (*indexUsed)[i] = true
            backtrack(nums, indexUsed, path, res)
            (*indexUsed)[i] = false
            *path = (*path)[:len(*path)-1]
        }
    }
}