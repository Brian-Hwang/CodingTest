
#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    int times;
    scanf("%d%*c", &times);
    for (int i = 0; i < times; i++)
    {
        int score = 0;
        string line;
        getline(cin, line);
        // cout << line << endl;
        int flag = 0;
        for (auto &chr : line)
        {
            if (chr == 'O')
            {
                score += (++flag);
                // printf("%d %d \n", score, flag);
            }
            else
                flag = 0;
        }
        printf("%d\n", score);
    }
    return 0;
}
