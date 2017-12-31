#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
	char s[1000000];
	scanf("%s", s);
	int len = strlen(s);
	long long pivot;
	for (int i =0; i< len; i++)
	{
		if (s[i] == '^')
		{
			pivot =  i;
		}
	}
	long long left = 0;
	long long right = 0;
	int i_char;
	
	for (int i =0; i< len; i++)
	{
		if (s[i] != '=' && s[i] != '^')
		{
			i_char = s[i] - '0';
			if (i < pivot)
			{
				left += ( i_char * (pivot -i));
			}
			else if (i > pivot)
			{
				right += ( i_char * (i-pivot));
			}
		}
	}
	if (left == right)
	{
		printf("balance");
	}
	else if  (left > right)
	{
		printf("left");
	}
	else
	{
		printf("right");
	}
}
