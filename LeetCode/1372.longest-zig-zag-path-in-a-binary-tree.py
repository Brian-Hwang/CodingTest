#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_count = 0

        def dfs(node, is_right, count):
            if not node:
                return

            self.max_count = max(self.max_count, count)
            dfs(node.right, True, 1 if is_right else count + 1)
            dfs(node.left, False, count + 1 if is_right else 1)

        dfs(root.right, True, 1)
        dfs(root.left, False, 1)

        return self.max_count


# @lc code=end
