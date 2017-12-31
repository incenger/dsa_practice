#include <stdio.h>

int main(void) {
	// calculate all cases
	// find min
	int n;
	scanf("%d\n", &n);
	int cash[100][102];
	int sum[100] = {0};
	for (int i = 0; i < n; i++)
	{
		scanf("%d ", &cash[i][0]);
	}
	for (int i = 0; i < n; i++ )
	{
		for (int j = 1; j<= cash[i][0];j++)
		{
			scanf("%d ", &cash[i][j]);
		}
	}
	for (int i = 0; i <n ; i++)
	{
		sum[i] += 15*cash[i][0];
		for (int j = 1; j <= cash[i][0]; j++)
		{
			sum[i] += cash[i][j]*5;
		}
	}
	int min = sum[0];
	for (int i = 0; i <n; i++)
	{
		if (sum[i] < min)
		{
			min = sum[i];
		}
	}
	printf("%d", min);
}
