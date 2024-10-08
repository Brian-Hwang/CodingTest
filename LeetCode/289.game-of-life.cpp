/*
 * @lc app=leetcode id=289 lang=cpp
 *
 * [289] Game of Life
 */

// @lc code=start

// @problem define
// 1. under population (cel == 1 && nb <2)
// 2. live (cel == 1 && 2 <= nb <= 3)
// 3. over population (cel == 1 && 3 < nb)
// 4. reproduction (cel == 0 && nb == 3 )

// 5. Try to solve it in place!
// @algorithm
// To remain both current state and next state,
// we can set as alive-> dead : -1 // dead-> alive: 3
// that way, we can keep on track on both current and next state.
// Then, we can go over again and change the board.

// @ How-to
// Use 3 functions:
// 1. check neighbor live num
//  ==> check nb if not out of bound.
// 2. check next state
//  ==> if 0/1, use switch statement for 1.
// 3. finalize the board

// @ complexity
// O(n) tc/sc

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void liveOrDie(int i, int j, vector<vector<int>> &board, int alive)
    {
        // alive -> dead : 3
        if (board.at(i).at(j) >= 1 && (alive < 2 || alive > 3))
        {
            board.at(i).at(j) = 3;
        }

        // dead -> alive : -1
        else if (board.at(i).at(j) <= 0 && alive == 3)
        {
            board.at(i).at(j) = -1;
        }
    }

    int numOfAliveNeighbor(int i, int j, vector<vector<int>> &board)
    {
        int alive = 0;
        for (int k = -1; k <= 1; k++)
        {
            for (int l = -1; l <= 1; l++)
            {
                if ((k == 0 && l == 0) || i + k < 0 || j + l < 0 || i + k >= board.size() || j + l >= board.at(i).size())
                    continue;
                if (board.at(i + k).at(j + l) >= 1)
                    alive++;
            }
        }
        return alive;
    }

    void finalizeBoard(int i, int j, vector<vector<int>> &board)
    {
        if (board.at(i).at(j) == 3)
            board.at(i).at(j) = 0;
        else if (board.at(i).at(j) == -1)
            board.at(i).at(j) = 1;
    }

    void gameOfLife(vector<vector<int>> &board)
    {
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board.at(i).size(); j++)
            {
                int alive = numOfAliveNeighbor(i, j, board);
                liveOrDie(i, j, board, alive);
            }
        }

        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board.at(i).size(); j++)
            {
                finalizeBoard(i, j, board);
            }
        }
    }
};
// @lc code=end
