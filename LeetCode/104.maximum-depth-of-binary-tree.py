#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        visited = []
        queue = deque([(root, 1)])
        max_depth = 1
        while queue:
            n, depth = queue.popleft()
            if n not in visited:
                visited.append(n)
                if n.left:
                    max_depth = max(max_depth, depth + 1)
                    queue.append((n.left, depth + 1))
                if n.right:
                    max_depth = max(max_depth, depth + 1)
                    queue.append((n.right, depth + 1))
        return max_depth


# @lc code=end
