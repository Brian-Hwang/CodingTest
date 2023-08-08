#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0
        it = iter(enumerate(flowerbed))

        for i, flower in it:
            # If empty
            if flowerbed[i] == 0:
                # And next also 0
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    possible = possible + 1
                else:
                    next(it, None)
            next(it, None)
        return possible >= n


# @lc code=end
