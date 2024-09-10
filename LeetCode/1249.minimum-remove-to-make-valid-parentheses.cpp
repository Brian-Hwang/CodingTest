/*
 * @lc app=leetcode id=1249 lang=cpp
 *
 * [1249] Minimum Remove to Make Valid Parentheses
 */

using namespace std;
#include <istream>
#include <stack>
#include <string>
// @lc code=start
class Solution
{
public:
    string minRemoveToMakeValid(string s)
    {
        stack<int> stck;

        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == '(')
            {
                stck.push(i);
            }
            else if (s[i] == ')')
            {
                if (stck.empty())
                {
                    s[i] = '.';
                }
                else
                {
                    stck.pop();
                }
            }
        }

        while (!stck.empty())
        {
            s[stck.top()] = '.';
            stck.pop();
        }

        s.erase(remove(s.begin(), s.end(), '.'), s.end());

        return s;
    }
};
// @lc code=end
