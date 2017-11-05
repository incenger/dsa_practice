#include <stdio.h>

int panli(int a, int b)
{
	if ( a /10 == b%10 && a%10 == b/10)
	{
		return 0;
	}
	return 1;

}

int main(void) {
	// just check the hours
	int a,b;
	scanf("%d:%d", &a,&b);
	do
	{
		 b = (b+1) % 60;
		 if (b == 0)
		 {
		 	a = (a +1) % 24;
		 }
	}
	while (panli(a,b) != 0);
	if (a < 10)
	{
		printf("0%d", a);
	}
	else
	{
		printf("%d", a);
	}
	printf(":");
	if( b <9)
	{
		printf("0%d", b);
	}
	else
	{
		printf("%d", b);
	}

	
}
