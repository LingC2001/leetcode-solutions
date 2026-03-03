func generateParenthesis(n int) []string {
    res := []string{}
    backtrack(n, 0, 0, &[]string{}, &res)
    return res
}

func backtrack(n int, left int, right int, path *[]string, res *[]string) {
    if len(*path) == 2*n {
        *res = append(*res, strings.Join(*path, ""))
    }
    
    if left < n {
        *path = append(*path, "(")
        backtrack(n, left + 1, right, path, res)
        *path = (*path)[:len(*path)-1]
    }

    if right < left {
        *path = append(*path, ")")
        backtrack(n, left, right + 1, path, res)
        *path = (*path)[:len(*path)-1]
    }
}