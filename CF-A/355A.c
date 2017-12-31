#include <stdio.h>

int main(void) {
	// implement digit root function
	// increase until get required number
	int k,d;
	scanf("%d %d", &k, &d);
	if (d== 0)
	{
		if (k == 1)
		{
			printf("0");
			return 0;
		}
		else
		{
			printf("No solution");
			return 0;
		}
	}
	printf("%d", d);
	for(int i = 0; i < k-1; i++)
	{
		printf("0");
	}
	
}
