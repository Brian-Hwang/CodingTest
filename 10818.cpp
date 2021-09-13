#include <stdio.h>
#include <iostream>
#include <boost/algorithm/string.hpp>
#include <vector>
#include <climits>
#include <string.h>
using namespace std;
using namespace boost;
int main()
{
    int num, min = INT_MAX, max = INT_MIN;
    int *array;
    cin >> num;
    string input;
    std::getline(std::cin, input);
    cout << input << endl;
    vector<string> strs;
    boost::split(strs, input, boost::is_any_of(" "));
    cout << strs.size() << endl;
    for (size_t i = 0; i < num; i++)
    {
        int num = stoi(strs[i]);
        cout << strs[i] << endl;
        if (num < min)
            min = num;
        if (num > max)
            max = num;
    }

    cout << min << " " << max << endl;
}