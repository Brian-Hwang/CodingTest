#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # List num = 1
        if head == None or head.next == None:
            return head

        prev = head
        current = head.next
        prev.next = None

        if current.next == None:
            current.next = prev
            return current

        next = current.next

        while True:
            # change next dir
            current.next = prev

            # iterate
            prev = current
            current = next
            if next.next == None:
                break
            else:
                next = next.next

        current.next = prev

        return current


# @lc code=end
