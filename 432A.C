#include<stdio.h>

int main(void)
{
    int n;
    int k;
    scanf("%d %d", &n, &k);
    int y[n];
    for(int i = 0; i<n; i++)
    {
        scanf("%d", &y[i]);
    }
    //sorting
    int year[6] = {0};
    for (int i =0; i < n; i++)
    {
        year[y[i]]++;
    }
    int j =0;
    int i= 0;
    while (i < n)
    {
        if(year[j] != 0)
        {
            y[i]= j;
            year[j]--;
            i++;
        }
        else if (year[j] == 0)
        {
            j++;
        }
    }
    i = 0;
    int count = 0;
    while (i<n)
    {
        if ( (5 - y[i]) >= k && (5 - y[i+1]) >= k && (5 - y[i+2]) >= k)
        {
            count++;
            i +=3;
        }
        else
        {
            break;
        }
    }
    printf("%d", count);
}