/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
    nodes := []*TreeNode{root}

    for len(nodes) > 0 {
        // check if mirror
        l := 0
        r := len(nodes)-1
        for l < r {
            if (nodes[l] == nil && nodes[r] != nil) || ( nodes[l] != nil && nodes[r] == nil) {
                return false
            } else if nodes[l] != nil && nodes[r] != nil && (nodes[l].Val != nodes[r].Val) {
                return false
            }
            l++
            r--
        }

        // add child of all nodes
        next := make([]*TreeNode, 0)
        for _, node := range nodes {
            if node != nil {
                next = append(next, node.Left)
                next = append(next, node.Right)
            }
        }

        nodes = next

    }
    
    return true

}
