#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#


# @lc code=start
class Solution:
    def __init__(self):
        self.memo = {}

    def breakWord(self, s, wordDict):
        if s in self.memo:
            return self.memo[s]

        for word in wordDict:
            index = s.find(word)
            if index != -1:
                if s == word:
                    return True
                left = right = True
                if index != 0:
                    left = self.breakWord(s[:index], wordDict)
                if index + len(word) != len(s):
                    right = self.breakWord(s[index + len(word) :], wordDict)
                if left and right:
                    self.memo[s] = True
                    return True
                else:
                    self.memo[s] = False

        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        return self.breakWord(s, wordDictSet)


# @lc code=end
