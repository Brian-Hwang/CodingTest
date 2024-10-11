/*
 * @lc app=leetcode id=49 lang=cpp
 *
 * [49] Group Anagrams
 */

// @lc code=start



// @Problem Description
// group anagrams

// @Algorithm
// Use Hashmap
// Sort the string in alphabet order
// Use the sorted string as key // use the unsorted as value
// append the values to the result

// @Complexity
// N = # strs // M = length of each str 
// sort string = O(n * mlogm)
// hashing = O(N)
// Thus O(N MlogM) => time
//space => hashmap O(N*M)


using namespace std;
#include <iostream>
#include <vector>
#include <unordered_map>

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> hashmap;
        for (auto &str : strs)
        {
            string sortedstr = str;
            sort(sortedstr.begin(), sortedstr.end());
            hashmap[sortedstr].push_back(str);
        }
        for (auto &entry : hashmap)
        {
            result.push_back(entry.second);
        }
        return result;
    }
};
// @lc code=end
