#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.found = False
        self.final_ancestor_node = root

        def dfs(node, ancestor):
            if not node:
                return
            print(node.val)

            if self.found:
                if (self.found == "p" and node.val == q.val) or (
                    self.found == "q" and node.val == p.val
                ):
                    self.final_ancestor_node = ancestor
                    print(self.final_ancestor_node, ancestor)
                    return
            else:
                if node.val == p.val:
                    self.found = "p"
                    ancestor = node
                elif node.val == q:
                    self.found = "q"
                    ancestor = node

            dfs(node.left, ancestor)
            dfs(node.right, ancestor)

        dfs(root, root)
        return self.final_ancestor_node


# @lc code=end
