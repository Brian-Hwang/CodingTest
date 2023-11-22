#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, target):
            if not node:
                return ([], 0)

            left_list, left_count = dfs(node.left, target)
            right_list, right_count = dfs(node.right, target)

            list = [x + node.val for x in (left_list + right_list)] + [node.val]
            count = left_count + right_count

            if target in list:
                count += list.count(target)

            return (list, count)

        _, count = dfs(root, targetSum)
        return count


# @lc code=end
