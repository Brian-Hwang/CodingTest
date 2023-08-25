#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxs = avgSum = sum(nums[0:k])
        for i in range(k, len(nums)):
            avgSum = avgSum + nums[i] - nums[i - k]
            maxs = max(maxs, avgSum)

        return maxs / k


# @lc code=end
