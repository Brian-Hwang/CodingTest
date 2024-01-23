#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        print(path)
        components = path.split("/")
        print(components)

        ans = ""
        for component in components:
            ans += component + "/"
        print(ans, ans[:-2])
        return ans[:-2]


# @lc code=end
