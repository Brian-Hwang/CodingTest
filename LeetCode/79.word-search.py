#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.board = None
        self.word = None

    def valid(self, x, y):
        if 0 > x or x >= self.m or 0 > y or y >= self.n:
            return False

        return True

    def possible(self, i, j, pos, visited):
        if (i, j) in visited:
            return False
        else:
            visited.add((i, j))

        if pos == len(self.word):
            return True

        possible = ((-1, 0), (1, 0), (0, 1), (0, -1))

        for step_x, step_y in possible:
            next_x, next_y = step_x + i, step_y + j
            if self.valid(next_x, next_y):
                print("NEXT: ", next_x, next_y)
                if self.board[next_x][next_y] == self.word[pos]:
                    print("POSSIBLE: ", next_x, next_y)
                    # visited.add((next_x, next_y))
                    if self.possible(next_x, next_y, pos + 1, visited):
                        return True
                    else:
                        print(visited)
                        # visited.remove((next_x, next_y))

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        # print(self.m, self.n)
        self.board = board
        self.word = word

        for i, row in enumerate(board):
            for j, box in enumerate(row):
                if box == word[0]:
                    visited = set()
                    print("BOX: ", i, j)
                    if self.possible(i, j, 1, visited):
                        return True

        return False


# ABCE
# SFCS
# ADEE

# ABCE
# SFES
# ADEE


# @lc code=end
