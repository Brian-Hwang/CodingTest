/*
 * @lc app=leetcode id=57 lang=cpp
 *
 * [57] Insert Interval
 */

// 1. first check where the interval is going to overlap
// 2. If not, push it back into the result vector.
// 3. If overlap, change the "new vector" with the min(start), max(end)
// 4. if latter does not overlap, insert.

// overlap
// [                         ]
//           [       ]
//      [       ]
//         [ ]
//  [      ]

// 1. both bigger // both smaller
// 2. one of them insied
// => new_start in border ||  new_end in border || both out of boarder

#include <vector>
#include <iostream>

using namespace std;

// @lc code=start
class Solution
{
public:
    int overlap(int new_start, int new_end, int start, int end)
    {
        int overlap = 0;
        if ((start <= new_start && new_start <= end) || (start <= new_end && new_end <= end) || (new_end >= end && new_start <= start))
        {
            overlap = 1;
        }

        return overlap;
    }

    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        vector<vector<int>> result;
        if (!intervals.size())
        {
            result.push_back(newInterval);
            return result;
        }

        int new_start = newInterval.at(0), new_end = newInterval.at(1);
        int continue_flag = 0;

        for (auto interval : intervals)
        {
            int start = interval.at(0), end = interval.at(1);
            // overlap
            if (!continue_flag && overlap(new_start, new_end, start, end))
            {
                new_start = min(start, new_start);
                new_end = max(end, new_end);
            }
            else
            {
                if (!continue_flag && new_end <= start)
                {
                    result.push_back({new_start, new_end});
                    continue_flag = 1;
                }
                result.push_back({start, end});
            }
        }
        if (!continue_flag)
        {
            result.push_back({new_start, new_end});
        }
        return result;
    }
};
// @lc code=end
