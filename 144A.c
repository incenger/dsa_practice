#include<stdio.h>
void swap(int *x, int *y);


int main (void)
{
    int n;
    scanf("%d", &n);
    int number[n];
    for(int i = 0; i< n; i++)
    {
        scanf("%d", &number[i]);
    }
    int max = number[0];
    int min = number[0];
    int i_max;
    int i_min;
    int count = 0;
    for(int i = 0; i< n; i++)
    {
        if(number[i] > max)
        {
            max = number[i];
        }
        if(number[i] < min)
        {
            min = number[i];
        }
    }
    for(int i = 0; i< n; i++)
    {
        if(number[i] == max)
        {
            i_max = i;
            break;
        }
    }
    while(number[0] != max)
    {
        swap(&number[i_max], &number[i_max -1]);
        i_max -= 1;
        count++;
    }
    for(int i = 0; i < n; i ++)
    {
        if (number[i] == min)
        {
            i_min = i;
        }
    }
    while(number[n-1] != min)
    {
        swap(&number[i_min], &number[i_min +1]);
        i_min += 1;
        count++;
    }
    printf("%d", count);
}

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
