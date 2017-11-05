#include <stdio.h>

int main(void) {
	// sorting the sockets of the filters
	// add sockets untill >= devices
	int n,m,k;
	scanf("%d %d %d\n", &n, &m, &k);
	int filter[50];
	for (int i = 0; i < n; i++)
	{
		scanf("%d ", &filter[i]);
	}
	int temp;
	for (int i = 0; i < n-1; i++)
	{
		for (int j = 0; j < n-1-i; j++)
		{
			if (filter[j] < filter[j+1])
			{
				temp = filter[j+1];
				filter[j+1] = filter[j];
				filter[j] = temp;
			}
		}
	}
	if (k >= m)
		{
			printf("0");
			return 0;
		}
	for (int i = 0; i<n; i++)
	{
		k = k + filter[i] -1;
		
		if (k >= m)
		{
			printf("%d", i+1);
			return 0;
		}
	}
	printf("-1");
}
