#include <stdio.h>

int removezeros(int n)
{
	int result = 0;
	int pow = 1;
	while (n > 0)
	{
		if (n % 10 != 0)
		{
			result += (n % 10)*pow;
			pow *= 10;
		}
		n /= 10;
	}
	return result;
}

	

int main(void) {
	// remove zero and check
	int a,b;
	scanf ("%d %d", &a, &b);
	int c =  a + b;
	if (removezeros(a) + removezeros(b) == removezeros(c))
	{
		printf("YES");
	}
	else 
	{
		printf("NO");
	}
}
