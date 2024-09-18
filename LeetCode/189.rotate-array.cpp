/*
 * @lc app=leetcode id=189 lang=cpp
 *
 * [189] Rotate Array
 */

using namespace std;
#include <iostream>
#include <vector>

// @lc code=start
class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        k %= nums.size();
        vector<int> temp(nums.end() - k, nums.end());
        copy(nums.begin(), nums.end() - k, nums.begin() + k);
        copy(temp.begin(), temp.end(), nums.begin());
    }
};
// @lc code=end
