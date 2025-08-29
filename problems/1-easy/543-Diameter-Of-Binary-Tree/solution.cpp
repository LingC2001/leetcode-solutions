#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int max_diameter = 0;
int diameterOfBinaryTree(TreeNode* root) {
    max_diameter = 0;
    dfs(root);
    return max_diameter;
}

int dfs(TreeNode* root) {
    if (!root) {
        return -1;
    }
    
    int max_left = dfs(root->left);
    int max_right = dfs(root->right);

    max_diameter = max(max_diameter, max_left + max_right + 2);
    return max(max_left, max_right) + 1;

}