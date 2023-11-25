#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def changeto_leftmost_right(node, dir):
            if dir == "right":
                child = node.right
            elif dir == "left":
                child = node.left
            else:
                child = node

            temp = child.right
            if not temp.left:
                if dir == "right":
                    node.right = temp
                elif dir == "left":
                    node.left = temp

                temp.left = child.left
                return

            while temp.left.left:
                temp = temp.left

            child.val = temp.left.val
            temp.left = temp.left.right

        def changeto_left(node, dir):
            if dir == "right":
                node.right = node.right.left
            else:
                node.left = node.left.left

        if not root:
            return None

        if key == root.val:
            if not root.right and not root.left:
                return None
            elif root.right:
                if not root.right.left:
                    changeto_leftmost_right(root, "root")
                    return root.right
                else:
                    changeto_leftmost_right(root, "root")
            elif root.left:
                return root.left

        node = root
        while node.right or node.left:
            if key > node.val:
                if not node.right:
                    return root
                if key == node.right.val:
                    if node.right.right:
                        changeto_leftmost_right(node, "right")
                    elif node.right.left:
                        changeto_left(node, "right")
                    else:
                        node.right = None
                else:
                    node = node.right
            else:
                if not node.left:
                    return root
                if key == node.left.val:
                    if node.left.right:
                        changeto_leftmost_right(node, "left")
                    elif node.left.left:
                        changeto_left(node, "left")
                    else:
                        node.left = None
                else:
                    node = node.left

        return root


# @lc code=end
