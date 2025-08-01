#include <unordered_map>
using namespace std;


// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};


Node* copyRandomList(Node* head) {
    unordered_map<Node*, Node*> ori_to_copy = {{nullptr, nullptr}};
    Node* curr_node = head;
    Node* copy_node = nullptr;
    while (curr_node) {
        copy_node = new Node(curr_node->val);
        ori_to_copy.insert({curr_node, copy_node});
        curr_node = curr_node->next;
    }

    curr_node = head;
    while (curr_node) {
        copy_node = ori_to_copy[curr_node];
        copy_node->next = ori_to_copy[curr_node->next];
        copy_node->random = ori_to_copy[curr_node->random];
        curr_node = curr_node->next;
    }   

    return ori_to_copy[head];
}
