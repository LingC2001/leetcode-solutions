using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


TreeNode* invertTree(TreeNode* root) {
    if (root == nullptr) {
        return root;
    }
    
    dfs(root);
    return root;
}

void dfs(TreeNode* node) {
    if (node->left) {
        dfs(node->left);
    }
    if (node->right) {
        dfs(node->right);
    }

    TreeNode* temp = node->left;
    node->left = node->right;
    node->right = temp;
}