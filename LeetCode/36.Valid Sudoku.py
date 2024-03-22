class Solution:
    def isDuplicate(self, digit, num):
        new_num = digit ^ (1 << (num - 1))

        # Exist Duplicate
        if new_num < digit:
            return -1
        else:
            return new_num

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            digits_row = 1 << 9
            digits_col = 1 << 9
            for j in range(9):
                num_str_row = board[i][j]
                num_str_col = board[j][i]

                if num_str_row != ".":
                    digits_row = self.isDuplicate(digits_row, int(num_str_row))
                    if digits_row == -1:
                        return False

                if num_str_col != ".":
                    digits_col = self.isDuplicate(digits_col, int(num_str_col))
                    if digits_col == -1:
                        return False

        threeByThree = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for I in threeByThree:
            for J in threeByThree:
                digits = 1 << 9
                for i in I:
                    for j in J:
                        num_str = board[i][j]
                        if num_str != ".":
                            digits = self.isDuplicate(digits, int(num_str))
                            if digits == -1:
                                return False

        return True
