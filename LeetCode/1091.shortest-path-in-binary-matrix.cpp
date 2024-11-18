/*
 * @lc app=leetcode id=1091 lang=cpp
 *
 * [1091] Shortest Path in Binary Matrix
 */
#include <vector>
#include <iostream>
#include <utility>
#include <queue>
#include <tuple>

using namespace std;

// Finding shortest path => Use BFS Search => Use Queue
// 1. Start with (0,0)
// 2. Get 8-directions (should do boundary check)
// 3. Should take in count of the "visited"
// 4. if reach last, return len. Else, return -1

// @lc code=start
class Solution
{
public:
    int shortestPathBinaryMatrix(vector<vector<int>> &grid)
    {
        int n = grid[0].size();
        if (grid.at(0).at(0) || grid.at(n - 1).at(n - 1))
            return -1;

        vector<pair<int, int>> direction = {{1, 1}, {1, 0}, {1, -1}, {0, 1}, {0, -1}, {-1, 1}, {-1, 0}, {-1, -1}};
        // row, col, length
        queue<tuple<int, int, int>> bfs;
        bfs.push({0, 0, 1});
        grid.at(0).at(0) = 1;

        while (!bfs.empty())
        {
            auto [x, y, len] = bfs.front();
            bfs.pop();
            if (x == n - 1 && y == n - 1)
                return len;
            for (auto dir : direction)
            {
                auto [dir_x, dir_y] = dir;
                int new_x = x + dir_x, new_y = y + dir_y;
                if (new_x >= 0 && new_x <= n - 1 && new_y >= 0 && new_y <= n - 1)
                {
                    if (grid.at(new_x).at(new_y) == 0)
                    {
                        grid[new_x][new_y] = 1;
                        bfs.push({new_x, new_y, len + 1});
                    }
                }
            }
        }

        return -1;
    }
};
// @lc code=end
