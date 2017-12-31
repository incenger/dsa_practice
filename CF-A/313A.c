#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int digit = abs(n) % 10;
    int last_delete = n/10;
    int prelast_delete = n/100;
    if (n >= 0)
    {
        printf("%d", n);
        return 0;
    }
    else if(n< 0 )
    {
        prelast_delete = prelast_delete*10 - digit;
    }
    
    if (last_delete > prelast_delete)
    {
        printf("%d", last_delete);
    }
    else
    {
        printf("%d", prelast_delete);
    }
}