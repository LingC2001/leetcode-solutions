type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p == nil && q == nil {
        return true
    } else if (p == nil && q != nil) || (p != nil && q == nil) {
        return false
    }
    
    if p.Val != q.Val {
        return false
    }
    var left bool = isSameTree(p.Left, q.Left)
    if !left {
        return false
    }
    var right bool = isSameTree(p.Right, q.Right)
    if !right {
        return false
    }
    return true
}