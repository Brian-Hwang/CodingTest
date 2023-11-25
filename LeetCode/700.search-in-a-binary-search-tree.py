#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        while True:
            if not node or val == node.val:
                return node
            if val > node.val:
                node = node.right
            else:
                node = node.left


# @lc code=end
