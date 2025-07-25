using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* getMidNode(ListNode* head);
ListNode* reverseList(ListNode* head);

void reorderList(ListNode* head) {
    // get middle node
    ListNode* mid = getMidNode(head);
    // reverse second half
    ListNode* reversed = reverseList(mid);
    
    // interleave nodes from head and reversed 
    ListNode dummy_head = ListNode(0, nullptr);
    ListNode* dummy_ptr = &dummy_head;
    // (note: reversed second half >= first half)
    while (head != mid) {
        // add node from first half
        dummy_ptr->next = head;
        dummy_ptr = dummy_ptr->next;
        head = head->next;

        // add node from reversed second half
        dummy_ptr->next = reversed;
        dummy_ptr = dummy_ptr->next;
        reversed = reversed->next;
    }
    if (reversed) dummy_ptr->next = reversed;
}

ListNode* getMidNode(ListNode* head)  {
    // find mid point
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

ListNode* reverseList(ListNode* head) {
    // reverse list
    ListNode* curr = head;
    ListNode* prev = nullptr;
    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}