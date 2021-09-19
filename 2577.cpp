#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <climits>
#include <string.h>
using namespace std;

int main()
{
    int th, num, final = 1;
    for (int i = 0; i < 3; i++)
    {
        cin >> num;
        final *= num;
    }
    string final_s = to_string(final);
    for (int i = 0; i < 10; i++)
    {
        cout << std::count(final_s.begin(), final_s.end(), char(i + 48)) << endl;
    }
}