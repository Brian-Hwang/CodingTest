#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        node = head
        while node.next != None:
            length += 1
            node = node.next

        if length == 1:
            return ListNode(val="", next=None)

        node = head
        for i in range(int(length / 2) - 1):
            node = node.next

        node.next = node.next.next

        return head


# @lc code=end
