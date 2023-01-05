class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        int numsSize = nums.size();
        for (int i = 1; i < numsSize; i++)
        {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};