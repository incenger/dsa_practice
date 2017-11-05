#include <stdio.h>

int main(void) {
	// count the number of 1..9
	// check if cucumber can press
	char a[4][4];
	int k;
	int panel[9]= {0};
	int temp;
	scanf("%d\n", &k);
	for (int i = 0; i<4; i++)
	{
		for (int j= 0; j < 4; j++)
		{
			scanf(" %c", &a[i][j]);
			if (a[i][j] != '.')
			{
				temp = a[i][j] - '0';
				panel[temp -1]++;
			}
		}
	}
	for (int i = 0; i < 9; i++)
	{
		if (panel[i] > k*2)
		{
			printf("NO");
			return 0;
		}
	}
	printf("YES");
}
