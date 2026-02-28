/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func pairSum(head *ListNode) int {
    var prev *ListNode
    cur := head
    fast := head
    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next
        next := cur.Next
        cur.Next = prev
        prev = cur
        cur = next
    }
    maximum := 0
    for prev != nil {
        maximum = max(maximum, prev.Val + cur.Val)
        prev = prev.Next
        cur = cur.Next
    }
    return maximum
}