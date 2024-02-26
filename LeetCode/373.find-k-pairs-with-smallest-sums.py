#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#


# @lc code=start
class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        ans = []
        smallest_list = []
        biggest_list = []
        new_dict = {}

        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                two_sum = nums1[i] + nums2[j]
                if len(smallest_list) < k or two_sum < -biggest_list[0]:
                    heapq.heappush(biggest_list, -two_sum)
                    heapq.heappush(smallest_list, two_sum)
                    if two_sum in new_dict:
                        new_dict[two_sum].append((nums1[i], nums2[j]))
                    else:
                        new_dict[two_sum] = [(nums1[i], nums2[j])]

        while len(ans) < k:
            smallest = smallest_list[0]
            for i in range(len(new_dict[smallest])):
                if len(ans) >= k:
                    return ans
                heapq.heappop(smallest_list)
                ans.append(new_dict[smallest][i])

        return ans[:k]


# @lc code=end
