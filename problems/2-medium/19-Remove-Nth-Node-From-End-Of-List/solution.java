public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        for (int i = 1; i < n; i++) {
            fast = fast.next;
        }

        while (fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next;
        }
           
        if (prev == null) {
            head = head.next;
        } else {
            prev.next = slow.next;
        }

        return head;
        
    }
}
