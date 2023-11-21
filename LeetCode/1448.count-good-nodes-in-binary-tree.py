#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, path_max):
            if not node:
                return 0

            return_val = dfs(node.left, max(path_max, node.val)) + dfs(
                node.right, max(path_max, node.val)
            )

            if node.val >= path_max:
                return_val += 1

            return return_val

        return dfs(root, root.val)


# @lc code=end
