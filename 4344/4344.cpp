
#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    int times;
    scanf("%d%*c", &times);
    for (int i = 0; i < times; i++)
    {
        int times2, sum = 0;
        scanf("%d", &times2);
        int *arr = (int *)malloc(times2 * sizeof(int));
        for (int j = 0; j < times2; j++)
        {
            scanf("%d", &(arr[j]));
            sum += arr[j];
        }
        int pass = 0;
        for (int j = 0; j < times2; j++)
        {
            if ((double)arr[j] > (double)sum / (double)times2)
                pass++;
        }
        printf("%.3f%\n", double(pass) / (double)times2 * 100);
    }
}
