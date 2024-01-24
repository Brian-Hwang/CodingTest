#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

import heapq


# @lc code=start
class SmallestInfiniteSet:
    def __init__(self):
        self.infiniteHeap = []
        self.infiniteSet = set()
        for i in range(1, 1001):
            heapq.heappush(self.infiniteHeap, i)
            self.infiniteSet.add(i)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.infiniteHeap)
        self.infiniteSet.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.infiniteSet:
            heapq.heappush(self.infiniteHeap, num)
            self.infiniteSet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
