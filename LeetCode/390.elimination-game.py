#
# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#


# @lc code=start
class Solution:

    # def delete_num(self, sets, is_odd, nth, n):
    #     if_odd = 1 * is_odd
    #     initial = list(sets)[0] if nth % 4 == 0 else 1
    #     i = if_odd * nth + initial
    #     while i < n:
    #         print(nth, if_odd, i)
    #         if i in sets:
    #             sets.remove(i)
    #         if_odd += 2
    #         i = if_odd * nth + initial

    # def lastRemaining(self, n: int) -> int:
    #     if n <= 2:
    #         return n

    #     all = set()

    #     for i in range(n // 2):
    #         all.add(i * 2 + 1)

    #     print(all)

    #     i = 2
    #     while len(all) != 1:
    #         # to_the_right
    #         if i % 4 == 0:
    #             self.delete_num(all, 0, i, n)
    #         else:
    #             if len(all) % 2 == 0:
    #                 self.delete_num(all, 1, i, n)
    #             else:
    #                 self.delete_num(all, 0, i, n)
    #         print(all)
    #         i += 2

    #     print(all)
    #     return list(all)[0] + 1
    def lastRemaining(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 2
        all = set()

        # for i in range(n // 2):
        #     all.add(i * 2 + 1)

        if (n // 2) % 2 == 0:
            index = 1
        else:
            index = 3
        while index < n:
            # print(index)
            all.add(index)
            index += 4

        # print(all)

        to_right = 1
        while len(all) != 1:
            if to_right or len(all) % 2 == 1:
                start = 0
            else:
                start = 1

            i = 0
            temp_list = sorted(all)
            for var in temp_list:
                if i % 2 == start:
                    all.remove(var)
                i += 1

            to_right = (to_right + 1) % 2

            # print(all)

        return list(all)[0] + 1


# @lc code=end
