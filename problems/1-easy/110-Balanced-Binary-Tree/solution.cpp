#include <algorithm>
#include <cmath>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int balanced = true;
    bool isBalanced(TreeNode* root) {
        balanced = true;
        dfs(root);
        return balanced;
    }

    int dfs(TreeNode* root) {
        if (!balanced || root == nullptr) {
            return 0;
        }

        int left = dfs(root->left);
        int right = dfs(root->right);

        if (abs(left-right) > 1) {
            balanced = false;
        }
        return max(left, right) + 1;
    }
};