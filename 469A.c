#include<stdio.h>

int main (void)
{
    int n;
    scanf("%d", &n);
    int x_lvl;
    int y_lvl;
    
    scanf("%d", &x_lvl);
    int x[x_lvl];
    for (int i =0; i < x_lvl; i++)
    {
        scanf("%d", &x[i]);
    }
    scanf("%d", &y_lvl);
    int y[y_lvl];
    for (int i =0; i < y_lvl; i++)
    {
        scanf("%d", &y[i]);
    }
    int require[101] ={0};
    for (int i =0; i < x_lvl; i++)
    {
        require[x[i]] = 1;
    }
    for (int i =0; i < y_lvl; i++)
    {
        require[y[i]] = 1;
    }
    for (int i = 1; i < n +1; i++)
    {
        if (require[i] == 0)
        {
            printf("Oh, my keyboard!");
            return 0;
        }
    }
    printf("I become the guy.");
}