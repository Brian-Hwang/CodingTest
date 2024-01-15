#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        len_l1, len_l2 = 1, 1

        temp_node = l1
        while temp_node.next != None:
            temp_node = temp_node.next
            len_l1 += 1

        temp_node = l2
        while temp_node.next != None:
            temp_node = temp_node.next
            len_l2 += 1

        iter_num = 0
        if len_l1 >= len_l2:
            long_node = l1
            short_node = l2
            iter_num = len_l2
        else:
            long_node = l2
            short_node = l1
            iter_num = len_l1

        overFlow = False
        for i in range(iter_num):
            long_node.val += short_node.val
            if overFlow:
                long_node.val += 1
                overFlow = False

            if long_node.val >= 10:
                long_node.val -= 10
                overFlow = True

            if i == iter_num - 1:
                break

            long_node = long_node.next
            short_node = short_node.next

        while overFlow:
            if long_node.next == None:
                new_node = ListNode(val=1, next=None)
                long_node.next = new_node
                overFlow = False
            else:
                long_node = long_node.next
                long_node.val += 1
                overFlow = False
                if long_node.val >= 10:
                    long_node.val -= 10
                    overFlow = True

        if len_l1 >= len_l2:
            return l1
        else:
            return l2


# @lc code=end
