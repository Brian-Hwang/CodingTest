#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <climits>
#include <string.h>
using namespace std;

int main()
{
    int input[10];
    int in, cnt = 0;
    for (int i = 0; i < 10; i++)
    {
        input[i] = -1;
    }
    for (int i = 0; i < 10; i++)
    {
        cin >> in;
        int num = in % 42;
        if (find(begin(input), end(input), num) == end(input))
        {
            input[cnt] = num;
            cnt++;
        }
    }

    cout << cnt << endl;
}