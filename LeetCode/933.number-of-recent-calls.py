#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#


# @lc code=start
class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and t - 3000 > self.queue[0]:
            self.queue.pop(0)

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end
