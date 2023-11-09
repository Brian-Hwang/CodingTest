#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#


# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pair = 0
        rows = [tuple(row) for row in grid]
        row_counter = Counter(rows)

        column = tuple(zip(*grid))
        column_counter = Counter(column)

        for tupl in row_counter:
            if tupl in column_counter:
                pair += row_counter[tupl] * column_counter[tupl]

        return pair


# @lc code=end
