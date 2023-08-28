#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#


# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        for num in nums:
            try:
                nums.remove(k - num)
            except:
                continue


# @lc code=end
