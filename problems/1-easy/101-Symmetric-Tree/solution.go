/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    leftTraversal := make([]*int, 0)
    dfs(root.Left, &leftTraversal, true)
    rightTraversal := make([]*int, 0)
    dfs(root.Right, &rightTraversal, false)
    
    if len(leftTraversal) != len(rightTraversal) {
        return false
    }

    for i := 0; i < len(leftTraversal); i++ {
        if (leftTraversal[i] == nil && rightTraversal[i] != nil) || (leftTraversal[i] != nil && rightTraversal[i] == nil) {
            return false
        } else if leftTraversal[i] != nil && rightTraversal[i] != nil && *leftTraversal[i] != *rightTraversal[i] {
            return false
        }
    }
    return true
}


func dfs(root *TreeNode, traversal *[]*int, leftFirst bool) {
    if root == nil {
        *traversal = append(*traversal, nil)
        return
    }

    if leftFirst {
        dfs(root.Left, traversal, leftFirst)
        dfs(root.Right, traversal, leftFirst)
    } else {
        dfs(root.Right, traversal, leftFirst)
        dfs(root.Left, traversal, leftFirst)
    }
    *traversal = append(*traversal, &root.Val) 
}