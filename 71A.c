//http://codeforces.com/problemset/problem/71/A

#include<stdio.h>
#include<string.h>



int main(void)
{
	
	int n;
	scanf("%d", &n);
	char word[100][101];
	for(int i =0; i < n; i++)
	{
		scanf("%s", word[i]);
	}
	for(int i =0; i < n; i++)
		{
			int l =  strlen(word[i]);
			if (l >10)
			{
				printf("%c%i%c\n", word[i][0], l-2, word[i][l-1]);
			}
			else
			{
				printf("%s\n", word[i]);
			}
		}
	
	
}
