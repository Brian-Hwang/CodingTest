#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        tree_queue = deque([root])
        result = [[root.val]]

        while len(tree_queue) != 0:
            level_result = []
            parent_num = len(tree_queue)

            for _ in range(parent_num):
                node = tree_queue.popleft()

                for children in node.children:
                    if children:
                        level_result.append(children.val)
                        tree_queue.append(children)

            if level_result:
                result.append(level_result)

        return result


# @lc code=end
