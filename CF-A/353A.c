#include <stdio.h>

int main(void) {
	// count the number of odd half
	// count the number of "rotate" half (which has one half is even and another is odd)
	// sum is even iff the number of odd halves is even
	int n;
	scanf("%d", &n);
	int up[100];
	int down[100];
	for (int i =0; i< n; i++)
	{
		scanf("%d %d", &up[i], &down[i]);
	}
	int odd_up =0;
	int odd_down = 0;
	int rota = 0;
	int result = 1;
	for (int i = 0; i < n; i++)
	{
		if (up[i] % 2 == 1)
		{
			odd_up ++;
		}
		if (down[i] % 2 == 1)
		{
			odd_down++;
		}
		if (up[i] % 2 == 1 && down[i] % 2 == 0)
		{
			rota++;
		}
		if (up[i] % 2 == 0 && down[i] % 2 == 1)
		{
			rota++;
		}
		
	}
	
	if (odd_up % 2 == 0 && odd_down % 2 == 0)
	{
		printf("0");
		return 0;
	}
	else if (odd_up % 2 == 1 && odd_down % 2 == 1)
	{
		if (rota > 0)
		{
			printf("1");
			return 0;
		}
		else
		{
			printf("-1");
			return 0;
		}
	}
	else
	{
		printf("-1");
		return 0;
	}
}
