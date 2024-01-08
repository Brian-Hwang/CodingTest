#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#


# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        def setNum():
            keypad = {i: [] for i in range(10)}
            print(keypad[0])
            keypad[0].extend([4, 6])
            keypad[1].extend([6, 8])
            keypad[2].extend([7, 9])
            keypad[3].extend([4, 9])
            keypad[4].extend([0, 3, 9])
            keypad[6].extend([0, 1, 7])
            keypad[7].extend([2, 6])
            keypad[8].extend([1, 3])
            keypad[9].extend([2, 4])
            return keypad

        ans = 0
        keypad = setNum()
        print(keypad)

        # for i in range(len(keypad)):
        #     paths = 1
        #     graph = deque([keypad[i]])
        #     for j in range(n - 1):
        #         node = graph.pop()
        #         print(node, len(node))
        #         paths *= len(node)

        #     ans += paths

        def dfs(node, start_num):
            for neighbor in keypad[node]:
                print(neighbor, end="")
                if neighbor == start_num:
                    print(start_num)
                else:
                    dfs(neighbor, start_num)
        
        print(0)
        dfs(0, 0)
        return ans


# @lc code=end
