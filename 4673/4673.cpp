#include <cstdio>
#include <iostream>

using namespace std;
#define N 10000
bool num[N + 1];
void check(int i);

int main()
{
    for (int i = 1; i < N; i++)
    {
        check(i);
    }
    for (int i = 1; i < N; i++)
    {
        bool print = num[i];
        if (!print)
            printf("%d\n", i);
    }
}

void check(int i)
{
    int result = i;
    while (i != 0)
    {
        result += i % 10;
        i /= 10;
        // printf("%d %d ", i, result);
    }
    printf("\n");
    if (result <= N)
        num[result] = true;
}