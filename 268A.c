#include<stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int a[n];
    int h[n];
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &h[i], &a[i]);
    }
    for (int i = 0; i < n-1; i++)
    {
        for (int j = i+1; j < n; j++)
        {
            if (h[i] == a[j] || a[i] == h[j])
            {
                count++;
            }
            if (h[i] == a[j] && a[i] == h[j])
            {
                count++;
            }
        }
    }
    printf("%d", count);
}