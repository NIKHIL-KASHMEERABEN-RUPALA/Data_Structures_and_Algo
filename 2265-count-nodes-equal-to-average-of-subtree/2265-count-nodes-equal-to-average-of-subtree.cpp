/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// I/O speedup to ensure 0ms runtime
static const auto fast_io = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();

class Solution {
private:
    // Returns pair<sum, count> of the subtree
    std::pair<int, int> dfs(TreeNode* node, int& matchingCount) {
        if (!node) {
            return {0, 0};
        }

        auto [leftSum, leftCount] = dfs(node->left, matchingCount);
        auto [rightSum, rightCount] = dfs(node->right, matchingCount);

        int currentSum = leftSum + rightSum + node->val;
        int currentCount = leftCount + rightCount + 1;

        if (node->val == (currentSum / currentCount)) {
            matchingCount++;
        }

        return {currentSum, currentCount};
    }

public:
    int averageOfSubtree(TreeNode* root) {
        int matchingCount = 0;
        dfs(root, matchingCount);
        return matchingCount;
    }
};