#include <stdio.h>

int main(void) {
	// print a table like this
	// BWBWBWBW
	// WBWBWBWB
	// BWWBWBWB
	// ........
	// replace bad cell
	int n;
	int m;
	scanf("%d %d", &n, &m);
	char inp[100][100];
	char out[100][100];
	for (int i = 0;  i <n; i++)
	{
		for (int j = 0;  j < m; j++)
		{
			scanf(" %c", &inp[i][j]);
		}
	}
	for (int i = 0;  i <n; i++)
	{
		for (int j = 0;  j < m; j++)
		{
			out[i][j] = inp[i][j];
			if (inp[i][j] == '.')
			{
				if (i % 2 == j % 2)
				{
					out[i][j] = 'B';
				}
				else if (i % 2 != j % 2)
				{
					out[i][j] = 'W';
				}
			}
		}
	}
	for (int i = 0; i <n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			printf("%c", out[i][j]);
		}
		printf("\n");
	}
}
