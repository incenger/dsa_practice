#include <stdio.h>

int main(void) {
	int n;
	int c;
	scanf("%d %d", &n, &c);
	int day[99];
	for (int i = 0; i <n; i++)
	{
		scanf("%d", &day[i]);
	}
	int max = day[0] -day[1] -c;
	int temp;
	for (int i = 0; i < n-1; i++)
	{
		temp = day[i] - day[i+1] -c;
		if (temp > max)
		{
			max= temp;
		}
	}
	if (max > 0)
	{
		printf("%d", max);	
	}
	else
	{
		printf("0");
	}
	
}
