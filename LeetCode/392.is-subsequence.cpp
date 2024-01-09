/*
 * @lc app=leetcode id=392 lang=cpp
 *
 * [392] Is Subsequence
 */

// @lc code=start
class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int tLen = t.length(), sLen = s.length();
        if (tLen < sLen)
            return false;
        for (int i = 0, j = 0; i < tLen || j == sLen; i++)
        {
            if (t[i] == s[j])
            {
                j++;
                continue;
            }
            if (sLen - j >= tLen - i)
            {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end
