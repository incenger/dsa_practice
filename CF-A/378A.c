#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int a;
	int b;
	scanf("%d %d", &a, &b);
	int win = 0;
	int draw = 0;
	int lose = 0;
	for (int i = 1; i <= 6; i++)
	{
		if (abs(a-i) > abs(b-i))
		{
			lose++;
		}
		else if (abs(a-i) < abs(b-i))
		{
			win++;
		}
		else
		{
			draw++;
		}
	}
	printf("%d %d %d", win, draw, lose);
}
