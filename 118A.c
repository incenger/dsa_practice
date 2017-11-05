//http://codeforces.com/problemset/problem/118/A
#include<stdio.h>
#include<string.h>

int main(void)
{
    char word[101];
    char alph[26] = {0};
    
    alph['a'-'a'] = 1;
    alph['u'-'a'] = 1;
    alph['o'-'a'] = 1;
    alph['e'-'a'] = 1;
    alph['i'-'a'] = 1;
    alph['y'-'a'] = 1;
    scanf("%s", word);
    int length = strlen(word);
    for (int i = 0; i < length; i++)
    {
        if (word[i] >= 'A' && word[i] <= 'Z')
        {
            word[i] = word[i] + 32;
        }
    }
    int k = 0;
    
    for (int i = 0; i < length; i++)
    {
        if (alph[word[i]-'a'] != 1) // phu am
        {
            k +=2;
        }
    }
	char result[k+1];
	for (int i = 0; i < length; i++)
    {
        if (alph[word[i]-'a'] != 1) // phu am
        {
            result[k] = '.';
            result[k+1] = word[i];
        }
    }
		
    printf("%s", result);
}