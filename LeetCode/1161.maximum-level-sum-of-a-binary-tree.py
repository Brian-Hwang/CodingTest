#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        final_max = root.val
        current_level, max_level = 0, 1
        tree = deque([root])

        while tree:
            current_level += 1
            level = len(tree)
            local_sum = 0
            for _ in range(level):
                node = tree.popleft()
                local_sum += node.val
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            if local_sum > final_max:
                final_max = local_sum
                max_level = current_level

        return max_level


# @lc code=end
