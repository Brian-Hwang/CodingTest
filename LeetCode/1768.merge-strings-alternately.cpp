/*
 * @lc app=leetcode id=1768 lang=cpp
 *
 * [1768] Merge Strings Alternately
 */

// @lc code=start

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int strlen1 = word1.length(), strlen2 = word2.length();
        int shorter, shorterlen;
        if (strlen1 > strlen2){
            shorter = 2;
            shorterlen = strlen2;
        }
        else if(strlen1 < strlen2){
            shorter = 1;
            shorterlen = strlen1;
        }
        else{
            shorter == -1;
            shorterlen=strlen1;
        }


        string returnword;
        int cnt = 0;
        
        while (cnt<shorterlen){
            returnword += word1[cnt];
            returnword += word2[cnt];
            cnt++;
        }

        if (shorter){
            if (shorter == 2){
                returnword += word1.substr(cnt);
            }
            else{
                returnword += word2.substr(cnt);
            }
        }
        return returnword;


    }
};
// @lc code=end

