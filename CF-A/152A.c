#include <stdio.h>

int main(void) {
	int n,m;
	scanf("%d %d", &n, &m);
	int grade[100][100];
	int student[100] = {0};
	for (int i = 0; i <n; i++)
	{
		for(int j = 0; j<m; j++)
		{
			scanf("%1d", &grade[i][j]);
		}
	}
	int temp = 0;
	int max = 0;
	int j =0;
	for (int i = 0; i < m; i++)
	{
		max = 0;
		for (j = 0; j < n; j++)
		{
			if (grade[j][i] > max)
			{
				max = grade[j][i];
			}
		}
		for (j = 0; j <n;j++)
		{
			if (grade[j][i] == max)
			{
				student[j]++;
			}
		}
		
	}
	int count =0;
	for (int i = 0; i <100; i++)
	{
		if (student[i] != 0)
		{
			count++;
		}
	}
	printf("%d", count);
}
