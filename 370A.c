#include <stdio.h>
#include <stdlib.h>

int main(void) { 
	//the number of moves the rook is needed is 1 if are in same column or row, else is 2
	//the number of moves the bishop is 1 if they are in one diagonal, 2 if are in different diagonal and can't move if different color
	//the number of moves the king is needed is max (|r1-r2|, |c1-c2|)
	int r1,c1,r2,c2;
	scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
	int rook, bishop, king;
	if (r1 == r2 || c1 == c2)
	{
		rook = 1;
	}
	else
	{
		rook = 2;
	}
	int k1=  abs(r1-r2);
	int k2=  abs(c1-c2);
	if  (k1 >= k2)
	{
		king = k1;
	}
	else
	{
		king = k2;
	}
	int color1 = abs((r1 -c1)) % 2;
	int color2 = abs((r2 -c2)) % 2;
	if (color1 != color2)
	{
		bishop = 0;
	}
	else
	{
		if (r1 + c1 == r2+c2 || (r1-c1) == (r2-c2))
		{
			bishop = 1;
		}
		else
		{
			bishop = 2;
		}
	}
	printf("%d %d %d", rook, bishop, king);
	
	return 0;
}