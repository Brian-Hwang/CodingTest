#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        total_counter = head
        count = 0
        while total_counter:
            count += 1
            total_counter = total_counter.next

        count //= 2

        prev = None
        current = head

        while count > 0:
            nexts = current.next
            current.next = prev
            prev = current
            current = nexts

            count -= 1

        result = 0
        while current:
            result = max(result, current.val + prev.val)
            current = current.next
            prev = prev.next

        return result


# @lc code=end
