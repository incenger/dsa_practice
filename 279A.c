#include <stdio.h>

int main(void) {
	int x,y;
	scanf("%d %d", &x, &y);
	if (x == 0 && y == 0)
	{
		printf("0");
		return 0;
	}
	if ( y <= 0 && x <= -y+1 && x >= y +1)
	{
		printf("%d", -y*4);
	}
	else if ( x > 0 &&  y >= -x +2 && y <= x)
	{
		printf("%d", x*4 -3);
	}
	else if (y > 0 && x<= y -1 && x >= -y)
	{
		printf("%d", y *4 -2);
	}
	else if (x < 0 && y <= - x +1 &&  y>= x -1)
	{
		printf("%d", -x*4 -1);
	}
	return 0;
}
