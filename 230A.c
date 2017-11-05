#include<stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main (void)
{
    int n;
    int s;
    scanf("%d %d", &s, &n);
    int x[n];
    int y[n];
    for(int i=0; i < n;  i++)
    {
        scanf("%d %d", &x[i], &y[i]);
    }
    
    for (int i= 0; i < n -1; i++)
    {
        for (int j = 0; j <n -1 -i; j++)
        {
            if (x[j] > x[j+1])
            {
                swap(&x[j], &x[j+1]);
                swap(&y[j], &y[j+1]);
            }
        }
    }
    
    for (int i = 0; i<n; i++)
    {
        if (s <= x[i])
        {
            printf("NO");
            return 0;
        }
        else
        {
            s = s + y[i];
        }
    }
    
    printf("YES");
    
    
}