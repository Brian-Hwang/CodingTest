#include <stdio.h>
#include <iostream>
#include <vector>
#include <climits>
#include <string.h>
using namespace std;
int main()
{
    int th, num, max = 0;
    for (int i = 0; i < 9; i++)
    {
        cin >> num;
        if (num > max)
        {
            max = num;
            th = i;
        }
    }
    cout << max << endl;
    cout << th + 1 << endl;
}