#include <stdio.h>

int main(void) {
	// if k >= 3n, the answer is 0
	// esle the answer is 3n - k
	int n,k;
	scanf("%d %d", &n, &k);
	if (k >= 3*n)
	{
		printf("0");
	}
	else
	{
		printf("%d", 3*n - k);
	}
	return 0;
}
