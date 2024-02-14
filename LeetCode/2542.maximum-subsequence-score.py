#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#
import heapq


# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # sum_nums1 = sum(nums1[:k])
        # min_nums2 = []
        # for i in range(k):
        #     heapq.heappush(min_nums2, nums2[i])

        # max_mult = sum_nums1 * min_nums2[0]
        # print(sum_nums1, min_nums2[0])
        # print(max_mult)
        # for i in range(k, length):
        #     sum_nums1 = sum_nums1 - nums1[i - k] + nums1[i]
        #     heapq.heappush(min_nums2, nums2[i])
        #     if min_nums2[0] == nums2[i - k]:
        #         heapq.pop(min_nums2)
        #     print(sum_nums1, min_nums2[0])
        #     print(max_mult)
        #     max_mult = max(max_mult, sum_nums1 * min_nums2[0])
        nums1_comb = list(combinations(nums1, k))
        nums2_comb = list(combinations(nums2, k))
        max_mult = 0
        for i in range(len(nums1_comb)):
            max_mult = max(max_mult, sum(nums1_comb[i]) * min(nums2_comb[i]))
        return max_mult


# @lc code=end
