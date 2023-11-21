#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1, tree2 = deque([root1]), deque([root2])
        leaf = []

        while tree1:
            n = tree1.pop()

            if not n.right and not n.left:
                leaf.append(n.val)
            else:
                if n.right:
                    tree1.append(n.right)
                if n.left:
                    tree1.append(n.left)
        while tree2:
            n = tree2.pop()
            if not n.right and not n.left:
                if not leaf or leaf[-1] != n.val:
                    return False
                else:
                    leaf.pop()
            else:
                if n.left:
                    tree2.append(n.left)
                if n.right:
                    tree2.append(n.right)

        return not leaf


# @lc code=end
