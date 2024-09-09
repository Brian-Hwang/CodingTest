/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

#include <iostream>
using namespace std;

// @lc code=start
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int end_ptr = m+n-1, nums1_ptr = m-1, nums2_ptr = n-1;
        for (int i=end_ptr; i>=0;i--){
            if (nums1_ptr==-1){
                while (end_ptr!=-1){
                    nums1.at(end_ptr--) = nums2.at(nums2_ptr--);
                }
                break;
            }

            if(nums2_ptr==-1){
                while(end_ptr!=-1){
                    nums1.at(end_ptr--) = nums1.at(nums1_ptr--);
                }
                break;
            }

            // nums1 bigger
            if (nums1.at(nums1_ptr) >= nums2.at(nums2_ptr)){
                nums1.at(end_ptr--) = nums1.at(nums1_ptr--);
            }
            else{
                nums1.at(end_ptr--) = nums2.at(nums2_ptr--);
            }

        }
    }
};
// @lc code=end

