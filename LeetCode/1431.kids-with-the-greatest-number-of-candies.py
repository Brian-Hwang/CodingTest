#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#


# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        canMax = []
        for i in range(len(candies)):
            # print(i)
            canMax.append(True if candies[i] + extraCandies >= max_candy else False)

        return canMax


# @lc code=end
