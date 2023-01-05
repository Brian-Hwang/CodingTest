#include <stdio.h>
#include <iostream>
#include <vector>
#include <climits>
#include <limits>
#include <string.h>
using namespace std;
int main()
{
    int num, max = -1;
    int *arr;
    cin >> num;
    arr = (int *)malloc(num * sizeof(int));
    for (int i = 0; i < num; i++)
    {
        int tmp;
        cin >> tmp;
        if (tmp > max)
            max = tmp;
        arr[i] = tmp;
    }
    float sum = 0;
    for (int i = 0; i < num; i++)
    {
        sum += float(arr[i]) / (float)max * 100.0f;
    }
    cout.precision(std::numeric_limits<double>::digits10 + 1);
    cout << sum / float(num) << endl;
}