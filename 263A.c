#include<stdio.h>
#include<stdlib.h>
int main(void)
{
    int number[5][5];
    for (int i = 0; i < 5; i++)
    {
        scanf("%d %d %d %d %d", &number[i][0], &number[i][1], &number[i][2], &number[i][3], &number[i][4]);
    }
    int row;
    int column;
    for (int i = 0; i < 5; i++)
    {
        for(int j =0; j < 5; j++)
        {
            if (number[i][j] == 1)
            {
               row = i;
               column = j;
            }
        }
    }
    int move = abs(row -2) + abs(column-2);
    printf("%d", move);
}