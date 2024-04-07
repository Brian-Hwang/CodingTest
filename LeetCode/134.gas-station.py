#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        possible = -1
        sub = []
        for i in range(n):

            sub.append(gas[i] - cost[i])

        print(sub)
        left = sub[0]
        right = sum(sub[1:])
        print(left, right)
        # for i in range(n):

        return possible


# @lc code=end
