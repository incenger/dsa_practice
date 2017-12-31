#include <stdio.h>

int prime(int n)
{
	if (n <=1)
	{
		return 1;
	}
	int i = 2;
	while (i*i <= n)
	{
		if ( n % i == 0)
		{
			return 1;
		}
		i++;
	}
	return 0;
}
int  phi(int n)
{
	int i = 1;
	float result = n;
	while (i <= n )
	{
		i++;
		if (n % i == 0 && prime(i) == 0)
		{
			result *=(1.0 - 1.0/ (float) i);
		}
	}
	return (int) result;
}	


int main(void) {
	// the answer is phi(p-1)
	int p;
	scanf("%d", &p);
	printf("%d", phi(p-1) );
}
