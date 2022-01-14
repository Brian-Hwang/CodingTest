
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
long long sum(std::vector<int> &a);

int main()
{
    std::vector<int> v = {7, 5, 16, 8};
    int a;
    a = sum(v);
    printf("%d", a);
    return 0;
}

long long sum(std::vector<int> &a)
{
    long long sum = 0;
    for (auto iter : a)
    {
        sum += iter;
    }
    return sum;
}
