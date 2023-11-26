#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0

        for city_index in range(len(isConnected)):
            if city_index in visited:
                continue
            need_visit = deque([city_index])
            provinces += 1
            while need_visit:
                visit_index = need_visit.pop()
                if visit_index not in visited:
                    visited.add(visit_index)
                    need_visit.extend(
                        i
                        for i, key in enumerate(isConnected[visit_index])
                        if key == 1 and i not in visited and i != visit_index
                    )

        return provinces


# @lc code=end
