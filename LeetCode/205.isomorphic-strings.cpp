/*
 * @lc app=leetcode id=205 lang=cpp
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        int sLen = s.length();
        int mapst[200] = {0};
        int mapts[200] = {0};
        for (int i = 0; i < sLen; i++)
        {
            if (mapst[t[i]] == 0 && mapts[s[i]] == 0)
            {
                mapst[t[i]] = s[i];
                mapts[s[i]] = t[i];
            }
            else
            {
                if (mapst[t[i]] == s[i] && mapts[s[i]] == t[i])
                    continue;
                else
                    return false;
            }
        }
        return true;
    }
};
// @lc code=end
