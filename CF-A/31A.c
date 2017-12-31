#include <stdio.h>

int main(void) {
	int n;
	int a[100];
	scanf("%d", &n);
	for (int i = 0; i<n; i++)
	{
		scanf("%d", &a[i]);
	}
	for (int i = 0;i < n;i++)
	{
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				if (i != j && j != k && i != k && a[i] == a[j] + a[k])
				{
					printf("%d %d %d", i+1, j+1, k+1);
					return 0;
				}
			}
		}
	}
	printf("-1");
}
