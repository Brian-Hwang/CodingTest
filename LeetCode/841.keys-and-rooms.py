#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#


# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []
        need_visited = deque([0])
        while need_visited:
            index = need_visited.pop()
            if index not in visited:
                visited.append(index)
                need_visited.extend(rooms[index])

        return len(visited) == len(rooms)


# @lc code=end
