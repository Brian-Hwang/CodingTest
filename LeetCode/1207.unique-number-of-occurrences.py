#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#


# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        elements = {}
        for element in arr:
            if element in elements:
                elements[element] += 1
            else:
                elements[element] = 1

        occurance = set()
        for element in elements:
            if elements[element] in occurance:
                return False
            occurance.add(elements[element])
        return True


# @lc code=end
