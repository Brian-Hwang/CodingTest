#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#


# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nondistinct = set(nums1).intersection(nums2)
        return [list(set(nums1) - set_nondistinct), list(set(nums2) - set_nondistinct)]


# @lc code=end
