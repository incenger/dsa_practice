#include<stdio.h>

int main(void)
{
    int a[3];
    for(int i = 0; i <3; i++)
    {
        scanf("%d", &a[i]);
    }
    int sum[4];
    sum[0] = a[0] + a[1] +a[2];
    sum[1] = a[0] * a[1] *a[2];
    sum[2] = (a[0] + a[1]) *a[2];
    sum[3] = a[0] * (a[1] +a[2]);
    int max = sum[0];
    for (int i =0; i < 4; i++)
    {
        if (sum[i] > max)
        {
            max = sum[i];
        }
    }
    printf("%d", max);
}