#include <stdio.h>

int main(void) {
	// if there is good cell on side column or side row, the answer is two
	// else the answer is four
	int n, m;
	scanf("%d %d", &n, &m);
	int cell[50][50];
	for (int i = 0; i< n;i++)
	{
		for (int j =0; j<m; j++)
		{
			scanf(" %d", &cell[i][j]);
		}
	}
	for (int i = 0; i < m; i++)
	{
		if (cell[0][i] == 1 || cell[n-1][i] == 1)
		{
			printf("2");
			return 0;
		}
	}
	for (int i = 0; i <n; i++)
	{
		if (cell[i][0] == 1 || cell[i][m-1] == 1)
		{
			printf("2");
			return 0;
		}
	}
	printf("4");
	return 0;
	
}
