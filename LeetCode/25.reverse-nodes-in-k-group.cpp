/*
 * @lc app=leetcode id=25 lang=cpp
 *
 * [25] Reverse Nodes in k-Group
 */

// @lc code=start

//  Definition for singly-linked list.
// struct ListNode
// {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

#include <iostream>
using namespace std;

class Solution
{
public:
    ListNode *reverseKGroup(ListNode *head, int k)
    {
        ListNode *tmp = head;
        int cnt = 0;
        while (tmp->next != nullptr)
        {
            ++cnt;
            tmp = tmp->next;
        }
        tmp = head;

        for (int i = 0; i < cnt / k; i++)
        {
            for (int j = 0; j < k; j++)
            {
                if (i == 0 && j == 0)
                    continue;
                cout << tmp->val;
                tmp = tmp->next;
            }

            cout << endl;
        }

        return head;
    }
};
// @lc code=end
