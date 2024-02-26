#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#


# @lc code=start
class Solution:
    def ComputeWith(self, left, right, operation):
        if operation == "+":
            return [x + y for x in left for y in right]
        elif operation == "-":
            return [x - y for x in left for y in right]
        elif operation == "*":
            return [x * y for x in left for y in right]

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        oper = "-+*"
        result = []
        for i, char in enumerate(expression):
            if char in oper:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1 :])
                result.extend(self.ComputeWith(left, right, char))

        return result


# @lc code=end
