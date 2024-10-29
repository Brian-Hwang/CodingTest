/*
 * @lc app=leetcode id=128 lang=cpp
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

// Check for n-1 or n+1 if in the hashmap
// If so, add to the sequence
// else,
// for instance if we have 5,6,7 ==> (5,7) and (7,5)

// So,
//  1. Make an unordered_map
//  2. start with 1 element (if no consec. exists)
//  3. If consec exists, add to that key (check former and latter)
//  4. if both former and latter exists, concat the two consecutives

// ex) n= 5 => if we have 6,7,8 => (5,8) // (8,5)
// ex2) n =5, we have 2,3,4 => (2,5) // (5,2)
// ex3) n =5, we have 2,3,4 & 6,7,8 => (2,8) (8,2)

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        if (!nums.size())
            return 0;

        unordered_map<int, int> hashmap;
        for (int i = 0; i < nums.size(); i++)
        {
            int n = nums.at(i);

            // duplicate
            if (hashmap.find(n) != hashmap.end())
                continue;

            // one below && one over both exists => concat the consecutives.
            if (hashmap.find(n + 1) != hashmap.end() && hashmap.find(n - 1) != hashmap.end())
            {
                int new_start = min({n - 1, hashmap[n - 1], hashmap[n + 1]});
                int new_end = max({n + 1, hashmap[n - 1], hashmap[n + 1]});
                hashmap.erase(hashmap[n - 1]);
                hashmap.erase(hashmap[n + 1]);
                hashmap.erase(n - 1);
                hashmap.erase(n + 1);
                hashmap[new_start] = new_end;
                hashmap[new_end] = new_start;
            }

            // exists one below // ex) n= 5 => if we have 6,7,8
            else if (hashmap.find(n + 1) != hashmap.end() && hashmap[n + 1] >= n + 1)
            {
                int start = n + 1, end = hashmap[n + 1], new_start = n;
                hashmap.erase(start);
                hashmap[new_start] = end;
                hashmap[end] = new_start;
            }
            // ex2) n =5, we have 2,3,4 => (2,3) // (4,2)
            else if (hashmap.find(n - 1) != hashmap.end() && hashmap[n - 1] <= n - 1)
            {
                int start = hashmap[n - 1], end = n - 1, new_end = n;
                hashmap.erase(end);
                hashmap[start] = new_end;
                hashmap[new_end] = start;
            }

            // no latter or former
            else
            {
                hashmap[n] = n;
            }
        }

        int max_result = 0;
        for (auto x : hashmap)
        {
            max_result = max(max_result, x.first - x.second);
        }

        return max_result + 1;
    }
};
// @lc code=end
