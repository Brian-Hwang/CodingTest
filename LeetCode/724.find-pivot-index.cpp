/*
 * @lc app=leetcode id=724 lang=cpp
 *
 * [724] Find Pivot Index
 */

// @lc code=start
class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int numsSize = nums.size();
        int left = 0, right = 0;

        for (int i = 1; i < numsSize; i++)
        {
            right += nums[i];
        }
        if (right == 0)
            return 0;

        for (int i = 1; i < numsSize; i++)
        {
            left += nums[i - 1];
            right -= nums[i];

            if (left == right)
                return i;
        }
        return -1;
    }
};
// @lc code=end
