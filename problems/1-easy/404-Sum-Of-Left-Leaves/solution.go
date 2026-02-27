/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func sumOfLeftLeaves(root *TreeNode) int {
    sum := 0
    dfs(root, false, &sum)
    return sum
}

func dfs(node *TreeNode, leftChild bool, sum *int) {
    if node.Left != nil {
        dfs(node.Left, true, sum)
    }
    if node.Right != nil {
        dfs(node.Right, false, sum)
    }

    if node.Left == nil && node.Right == nil && leftChild {
        *sum += node.Val
    }

}