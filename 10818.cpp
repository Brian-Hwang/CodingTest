#include <stdio.h>
#include <iostream>
#include <vector>
#include <climits>
#include <string.h>
using namespace std;
int main()
{
    int num, min = INT_MAX, max = INT_MIN;
    cin >> num;
    cin.ignore(256, '\n');
    string input;
    std::getline(std::cin, input);
    input += '\n';
    int start = 0U;
    int place = input.find(" ");

    while (place != string::npos)
    {
        int number = stoi(input.substr(start, place - start));
        if (number < min)
            min = number;
        if (number > max)
            max = number;
        start = place + 1;
        place = input.find(" ", start);
    }
    int number = stoi(input.substr(start, place - start));
    if (number < min)
        min = number;
    if (number > max)
        max = number;
    cout << min << " " << max << endl;
}