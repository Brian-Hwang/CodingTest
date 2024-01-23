#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeSort(first_half, second_half):
        if not first_half or not first_half.next:
            return first_half

        middle = find_middle(head)

        second_half = second_half.next

        second_half.next = None

        left = mergeSort(first_half)
        right = mergeSort(second_half)

        sorted_list = merge(left, right)
        return sorted_list

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        mid_node = head
        while temp.next and temp.next.next:
            mid_node = mid_node.next
            temp = temp.next.next

        return mergeSort(head, mid_node)


def find_middle(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(left, right):
    dummy = ListNode()
    tail = dummy
    while left and right:
        if left.value < right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left or right
    return dummy.next


# @lc code=end
