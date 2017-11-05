#include<stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int t[n];
    int math[5000] = {0};
    int program[5000] = {0};
    int pe[5000]= {0};
    for(int i =0; i < n; i++)
    {
        scanf("%d", &t[i]);
    }
    int a = 0;
    int b = 0;
    int c = 0;
    for (int i = 0;i<n ; i++)
    {
        switch(t[i])
        {
            case 1:
                program[a] = i +1;
                a++;
                break;
            case 2:
                math[b] = i+1;
                b++;
                break;
            case 3:
                pe[c] = i+1;
                c++;
                break;
        }
    }    
    
    int min = a;
    if (min > b)
    {
      min = b;  
    }
    if(min >c)
    {
        min = c;
    }
    for (int i = 0; i <min;i ++)
    {
        if (program[i] == 0 || math[i] == 0 || pe[i] == 0)
        {
            min =0;
        }
    }
    
    printf("%d\n", min);
    
    for (int i = 0; i <min;i ++)
    {
        printf("%d %d %d\n", program[i], math[i], pe[i]);
    }
}