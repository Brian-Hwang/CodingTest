#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        tree = deque([root])
        result = []

        while tree:
            level = len(tree)
            for _ in range(level - 1):
                node = tree.popleft()
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)

            rightmost_node = tree.popleft()
            result.append(rightmost_node.val)
            if rightmost_node.left:
                tree.append(rightmost_node.left)
            if rightmost_node.right:
                tree.append(rightmost_node.right)

        return result


# @lc code=end
