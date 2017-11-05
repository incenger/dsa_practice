#include <stdio.h>
#include <stdlib.h>

int lucky(int n)
{
	n = abs(n);
	while (n >0)
	{
		if (abs(n) % 10 == 8)
		{
			return 0;
		}
		n /= 10;
	}
	return 1;
}	

int main(void) {
	// increase b
	//check if current floor is lucky
	int n;
	scanf("%d", &n);
	int b =1;
	while (lucky(n + b) != 0)
	{
		b++;
	}
	printf("%d", b);
}
