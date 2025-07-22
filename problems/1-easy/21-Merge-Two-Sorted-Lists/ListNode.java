public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    
    ListNode dummy = new ListNode();
    ListNode current = dummy;

    while (list1 != null && list2 != null) {
        if (list2.val < list1.val) {
            current.next = list2;
            current = current.next;
            list2 = list2.next;
        } else {
            current.next = list1;
            current = current.next;
            list1 = list1.next;
        }

    }
    current.next = (list2 != null) ? list2 : list1;
    return dummy.next;
}
