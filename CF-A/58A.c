//http://codeforces.com/problemset/problem/58/A
#include<stdio.h>
#include<string.h>

int main(void)
{
    char word[100];
    char hello[5] = {'h','e','l','l','o'};
    
    int k = 0;
    scanf("%s", word);
    int length = strlen(word);

    for (int i = 0; i < length; i++)
        {
            if (word[i] == hello[k] && k < 5)
                {
                    k++;
                }
            if (k == 5)
            {
                break;
            }
        }
    
    if (k == 5)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
    
}