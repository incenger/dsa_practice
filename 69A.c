#include<stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int vector[n][3];
    for (int i =0; i<n; i++)
    {
        scanf("%d %d %d", &vector[i][0], &vector[i][1], &vector[i][2]);
    }
    int sum = 0;
    for (int i =0; i<3; i++)
    {
        for (int j =0; j < n; j++)
        {
            sum = sum + vector[j][i];
        }
        if (sum != 0)
        {
            printf("NO");
            return 0;
        }
    }
    printf("YES");
    
}