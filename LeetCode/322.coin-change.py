#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(coins)
        print(coins)

        minimum = float("inf")
        modular = deque()
        for coin in reversed(coins):

            used = amount // coin
            left = amount % coin
            if used != 0 and left != 0:
                modular.appendleft((left, used))
            if left == 0:
                minimum = min(minimum, used)
        while modular:
            print(modular)
            left, used = modular.pop()
            for coin in reversed(coins):
                new_used = left // coin
                new_left = left % coin
                print(new_left, new_used)

                # no diff
                if new_used != 0:
                    used += new_used
                    left = new_left
                    if left == 0:
                        minimum = min(minimum, used)
                    else:
                        modular.appendleft((left, used))

        if minimum != float("inf"):
            return minimum
        else:
            return -1


# @lc code=end
