/*
 * @lc app=leetcode id=1071 lang=cpp
 *
 * [1071] Greatest Common Divisor of Strings
 */

#include <iostream>
#include <string>
#include<numeric>
using namespace std;

// @lc code=start
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {

        string pattern = str1.substr(0,gcd(str1.length(), str2.length()));
        int patternLength = pattern.length();

        for (int i=0; i< str1.length() || i < str2.length() ; i+=patternLength){
            if ((i < str1.length() && pattern != str1.substr(i,patternLength)) 
            || (i < str2.length() && pattern != str2.substr(i,patternLength))) 
            return "";
        }

        return pattern;
    }
};
// @lc code=end

