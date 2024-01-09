#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#


# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0 for i in range(n + 3)]
        memo[1] = memo[2] = 1

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

        return memo[n]


# @lc code=end
