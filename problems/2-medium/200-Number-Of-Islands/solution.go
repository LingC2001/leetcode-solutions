func numIslands(grid [][]byte) int {
    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] == '1' {
                dfs(grid, i, j)
                count += 1
            }
        }
    }
    return count
}

func dfs(grid [][]byte, i int, j int) {
    if !isLand(grid, i, j) {
        return
    }
    grid[i][j] = '#'
    dfs(grid, i+1, j) // go down
    dfs(grid, i-1, j) // go up
    dfs(grid, i, j+1) // go right
    dfs(grid, i, j-1) // go left

}

func isLand(grid [][]byte, i int, j int) bool {
    m := len(grid)
    n := len(grid[0])
    if i >= 0 && i < m && j >= 0 && j < n && grid[i][j] == '1' {
        return true
    }
    return false
}