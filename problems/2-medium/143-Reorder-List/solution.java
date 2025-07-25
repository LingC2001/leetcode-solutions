public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public void reorderList(ListNode head) {
        
        ListNode mid = findMidNode(head);
        ListNode reversed_list = reverseList(mid);
        mergeTwoLists(head,reversed_list,mid);

    }

    private ListNode findMidNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
           
        return slow;
    }

    private ListNode mergeTwoLists(ListNode list1, ListNode list2, ListNode mid) {
    
        ListNode dummy = new ListNode();
        ListNode current = dummy;

        while (list2 != null && list1 != mid) {
            current.next = list1;
            current = current.next;
            list1 = list1.next;

            current.next = list2;
            current = current.next;
            list2 = list2.next;
        }

        if (list2 != null) {
            current.next = list2;
        }
        
        return dummy.next;

    }

    private ListNode reverseList(ListNode head) {

        ListNode prev = null;
        ListNode current = head;
        ListNode nxt = null;

        while (current != null) {
            nxt = current.next;
            current.next = prev;
            prev = current;
            current = nxt;
        }
        
        return prev;

    }



}