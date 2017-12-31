#include <stdio.h>

int main(void) {
	int n,a,b,c;
	scanf("%d %d %d %d", &n, &a, &b, &c);
	int x = n/a;
	int y = n/b;
	int k =0;
	int max = 0;
	int temp;
	for (int i =0; i <= x; i++)
	{
		for (int j = 0; j <= y; j++)
		{
			k = (n -a*i - b*j) / c;
			if (a*i + b*j + k*c == n && k >= 0)
				{
					temp = i + j +k;
					if (temp > max)
					{
						max = temp;
					}
				}
		}
	}
	printf("%d", max);
}
