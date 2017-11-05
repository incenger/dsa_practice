#include<stdio.h>
#include<string.h>

int main (void)
{
    int number;
    scanf("%d", &number);
    int lucky[14] = {4 , 7, 47, 44 , 74, 77, 444, 447, 474, 744, 477, 747, 774, 777};
    for (int i = 0; i < 14; i++)
    {
        if (number % lucky[i] == 0)
        {
            printf("YES");
            return 0;
        }
    }
    printf("NO");
}

