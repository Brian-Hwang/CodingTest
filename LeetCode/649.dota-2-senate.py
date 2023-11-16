#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#


# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque(), deque()
        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)
        senate_len = len(senate)

        while radiant and dire:
            if radiant[0] > dire[0]:
                dire.append(dire[0] + senate_len)
            else:
                radiant.append(radiant[0] + senate_len)
            radiant.popleft()
            dire.popleft()

        if radiant:
            return "Radiant"
        else:
            return "Dire"


# @lc code=end
