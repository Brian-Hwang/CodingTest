#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#


# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lefts = []
        rights = []
        for asteroid in asteroids:
            # rights
            if asteroid > 0:
                rights.append(asteroid)

            # lefts
            else:
                flag = 0
                while len(rights) != 0:
                    if abs(asteroid) > rights[-1]:
                        rights.pop()
                    else:
                        if abs(asteroid) == rights[-1]:
                            rights.pop()
                        flag = 1
                        break
                if len(rights) == 0 and flag == 0:
                    lefts.append(asteroid)

        return lefts + rights


# @lc code=end
