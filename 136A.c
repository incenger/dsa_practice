#include<stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int giver[n];
    int receiver[n];
    for (int i = 0; i<n; i++)
    {
        scanf("%d", &giver[i]);
    }
    for (int i = 0; i <n;i++)
    {
        receiver[giver[i]-1] = i +1;
    }
    for (int i = 0; i < n; i++)
    {
        if (i != n-1)
        {
            printf("%d ", receiver[i]);
        }
        else
        {
            printf("%d", receiver[i]);
        }
    }
    
}