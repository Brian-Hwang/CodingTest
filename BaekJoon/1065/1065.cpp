#include <cstdio>
#include <iostream>

using namespace std;
bool check(int i);
int main()
{
    freopen("input.txt", "r", stdin);
    int N;
    scanf("%d", &N);
    int result = 0;
    for (int i = 1; i <= N; i++)
    {
        if (check(i))

            result++;
    }
    printf("%d", result);
    return 0;
}

bool check(int i)
{
    int last = i % 10, curr, diff = -10;

    while (i >= 10)
    {
        i /= 10;
        curr = i % 10;
        if (diff != -10 && diff != curr - last)
        {
            return false;
        }
        diff = curr - last;
        last = curr;
    }
    return true;
}
