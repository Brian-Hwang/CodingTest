#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1) 000
        # 2) 0 -x x
        # 3) -z -y z+y
        # 4) -x -x 2x

        nums = sorted(nums)
        neg = set()
        pos = set()
        zero = set()
        duplicates = set()
        ans = []

        for num in nums:
            if num == 0:
                if num in zero:
                    if num in duplicates:
                        ans.append(([0, 0, 0])
                    else:
                        duplicates.add(num)
                else:
                    zero.add(num)
            elif num <= 0:
                if num in neg:
                    duplicates.add(num)
                else:
                    neg.add(num)
            else:
                if num in pos:
                    duplicates.add(num)
                else:
                    pos.add(num)

        print(nums)
        print(neg)
        print(pos)
        print(zero)
        print(duplicates)
        if zero:
            for num in pos:
                if -num in neg:
                    ans.append(([0, num, -num]))

        print(ans)
        for num in pos:
            for second_num in pos:
                if second_num == num:
                    continue
                else:
                    if -1 * (num + second_num) in neg:
                        ans.append((num, second_num, -(num + second_num)))

        print(ans)
        for num in neg:
            for second_num in neg:
                if second_num == num:
                    continue
                else:
                    if -1 * (num + second_num) in pos:
                        ans.append((num, second_num, -(num + second_num)))

        print(ans)
        for dup in duplicates:
            if (dup > 0 and dup * -2 in neg) or (dup < 0 and dup * -2 in pos):
                ans.append((dup, dup, dup * -2))

        print(ans)

        return ans


# @lc code=end
