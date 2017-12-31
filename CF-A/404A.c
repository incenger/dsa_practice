#include <stdio.h>
#include <string.h>
int main(void) {
	
	int n;
	char dig[600];
	char side[89000];
	scanf("%d\n", &n);
	int count_d = 0;
	int count_s = 0;
	for (int i = 0; i<n; i++)
	{
		for (int j = 0; j<n; j++)
		{
			if ( j == i || j == n -1 -i)
			{
				scanf(" %c", &dig[count_d]);
				count_d++;
			}
			else 
			{
				scanf(" %c", &side[count_s]);
				count_s++;
			}
		}
	}
	char dig_temp = dig[0];
	char side_temp = side[0];
	if (dig_temp == side_temp)
	{
		printf("NO");
		return 0;
	}
	for (int i = 0; i < count_d; i++)
	{
		if ( dig[i] != dig_temp )
		{
			printf("NO");
			return 0;
		}
	}
	for (int i =0; i < count_s; i++)
	{
		if ( side[i] != side_temp)
		{
			printf("NO");
			return 0;
		}
	}
	printf("YES");

}
