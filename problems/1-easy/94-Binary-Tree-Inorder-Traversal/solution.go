/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    nodesArr := []int{}
    dfs(root, &nodesArr)
    return nodesArr
}

func dfs(node *TreeNode, nodesArr *[]int){
    if node == nil {
        return
    }

    dfs(node.Left, nodesArr)
    *nodesArr = append(*nodesArr, node.Val)
    dfs(node.Right, nodesArr)

}