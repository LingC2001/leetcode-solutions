/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumRootToLeaf(root *TreeNode) int {
    binary_num := make([]int, 0)
    sum := 0
    dfs(root, &binary_num, &sum)
    return sum
}


func dfs(root *TreeNode, binaryNum *[]int, sum *int) {
    if root == nil {
        return
    }
    *binaryNum = append(*binaryNum, root.Val)
    dfs(root.Left, binaryNum, sum)
    dfs(root.Right, binaryNum, sum)

    if root.Left == nil && root.Right == nil {
        *sum += convertBinaryToInt(*binaryNum)
    }
    *binaryNum = (*binaryNum)[:len(*binaryNum)-1]

}

func convertBinaryToInt(binaryNum []int) int {
    num := 0
    n := len(binaryNum)
    for i := n-1; i >= 0; i-- { 
        num += int(float64(binaryNum[i]) * math.Pow(2, float64(n-i-1)))
    } 
    return num 
}