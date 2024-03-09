class Solution:
    def is_big(self, x, y, a, b):
        if a > x:
            return True
        elif a == x:
            if b < y:
                return True
        return False

    def removed(self, set_xy, x, y):
        discard_list = set()
        for x_from_set, y_from_set in set_xy:
            if (
                self.is_big(x, y, x_from_set, y_from_set)
                or x_from_set == x
                or y_from_set == y
                or abs(y - y_from_set) == abs(x - x_from_set)
            ):
                discard_list.add((x_from_set, y_from_set))
        return set_xy - discard_list

    def select_possible(self, set_xy, n, trial):
        if n == trial:
            return len(set_xy)

        count = 0
        for x, y in set_xy:
            count += self.select_possible(self.removed(set_xy, x, y), n, trial + 1)
        return count

    def totalNQueens(self, n: int) -> int:
        set_xy = set((x, y) for x in range(n) for y in range(n))
        return self.select_possible(set_xy, n, 1)
