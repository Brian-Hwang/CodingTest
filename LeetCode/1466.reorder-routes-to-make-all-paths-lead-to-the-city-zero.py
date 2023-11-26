#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#


# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []
        original = set()
        for dir in connections:
            original.add((dir[0], dir[1]))
            graph[dir[0]].append(dir[1])
            graph[dir[1]].append(dir[0])

        fix = 0
        for path in graph[0]:
            if (0, path) in original:
                fix += 1
            visited = set([0])
            need_visit = deque([path])
            while need_visit:
                city = need_visit.pop()
                if city not in visited:
                    visited.add(city)
                    for new_city in graph[city]:
                        if new_city not in visited:
                            need_visit.append(new_city)
                            if (city, new_city) in original:
                                fix += 1

        return fix


# @lc code=end
