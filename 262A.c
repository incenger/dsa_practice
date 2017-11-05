#include <stdio.h>

int luckydigits(int n)
{
	int count = 0;
	while (n > 0)
	{
		if (n % 10 ==4 || n % 10 == 7)
		{
			count++;
		}
		n /= 10;
	}
	return count;
}

int main(void) {
	int n;
	int k;
	int number;
	int count =0;
	scanf("%d %d", &n, &k);
	for(int i =0; i< n; i ++)
	{
		scanf("%d", &number);
		if (luckydigits(number) <= k)
		{
			count++;
		}
	}
	printf("%d", count);
}