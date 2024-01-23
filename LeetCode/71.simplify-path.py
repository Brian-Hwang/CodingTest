#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")

        direc = []
        for component in components:
            if component == "." or component == "":
                continue
            elif component == "..":
                if len(direc) != 0:
                    direc.pop()
            else:
                direc.append(component)

        return "/" + "/".join(direc)


# @lc code=end
