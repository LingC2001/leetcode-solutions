public class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

public boolean hasCycle(ListNode head) {
    ListNode current = head;
    ListNode nxt = head;

    while (current != null) {
        if (current.next == head) {
            return true;
        }
        nxt = current.next;
        current.next = head;
        current = nxt;
    }
    return false;
}
