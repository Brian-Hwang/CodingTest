/*
 * @lc app=leetcode id=215 lang=cpp
 *
 * [215] Kth Largest Element in an Array
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

// @lc code=start
class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        priority_queue<int, vector<int>, greater<int>> karr;

        for (int i = 0; i < k; i++)
        {
            karr.push(nums.at(i));
        }

        for (int i = k; i < nums.size(); i++)
        {
            if (nums.at(i) > karr.top())
            {
                karr.pop();
                karr.push(nums.at(i));
            }
        }

        return karr.top();
    }
};
// @lc code=end
