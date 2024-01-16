#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        newhead = Node(head.val)

        iter_newhead = newhead
        iter_head = head
        while iter_head.next:
            iter_head = iter_head.next
            newNode = Node(iter_head.val)
            iter_newhead.next = newNode
            iter_newhead = iter_newhead.next

        iter_newhead = newhead
        iter_newhead_slow = newhead
        iter_head = head
        iter_head_slow = head

        while iter_newhead:
            if iter_head.random == None:
                iter_newhead.random = None
            else:
                while iter_head_slow != iter_head.random:
                    iter_head_slow = iter_head_slow.next
                    iter_newhead_slow = iter_newhead_slow.next
                iter_newhead.random = iter_newhead_slow

                iter_newhead_slow = newhead
                iter_head_slow = head

            iter_head = iter_head.next
            iter_newhead = iter_newhead.next

        return newhead


# @lc code=end
