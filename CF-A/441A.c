#include<stdio.h>

int main(void)
{
    int n;
    int v;
    scanf("%d %d", &n, &v);
    int s[50][51];
    for (int i = 0; i <n; i++)
    {
        scanf("%d", &s[i][0]);
        for (int j = 1; j <= s[i][0]; j++)
        {
            scanf("%d", &s[i][j]);
        }
    }
    int dealer[50] = {0};
    for (int i = 0; i <n; i++)
    {
        for(int j = 1; j <= s[i][0]; j++)
        {
            if(v > s[i][j])
            {
                dealer[i] = 1;
            }
        }
    }
    int count = 0;
    for (int i = 0; i < 50; i++)
    {
        if(dealer[i] != 0)
        {
            count++;
        }
    }
    printf("%d\n", count);
    for(int i = 0; i< 50; i++)
    {
        if(dealer[i]!= 0)
        {
            printf("%d ", i+1);
        }
    }
}