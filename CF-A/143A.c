#include <stdio.h>

int main(void) {
	int r[2];
	int c[2];
	int d[2];
	scanf("%d %d\n", &r[0], &r[1]);
	scanf("%d %d\n", &c[0], &c[1]);
	scanf("%d %d\n", &d[0], &d[1]);
	int a[4];
	a[0] = (r[0] + c[0] - d[1])/2;
	if (a[0]*2 == r[0] + c[0] - d[1] && a[0] > 0)
	{
		a[1] = r[0]- a[0];
		a[2] = c[0] -a[0];
		a[3] = d[0] -a[0];
		if (a[2] + a[3] != r[1] || a[1] + a[3] != c[1])
		{
			printf("-1");
			return 0;
		}
		for (int i = 0; i < 4; i++)
		{
			if (a[i] > 9 || a[i] <1)
			{
				printf("-1");
				return 0;
			}
		}
		for (int i = 0; i < 3; i++)
		{
			for (int j = i+1; j <4; j++)
			{
				if (a[i] == a[j])
				{
					printf("-1");
					return 0;
				}
			}
		}
		printf("%d %d\n", a[0],a[1]);
		printf("%d %d\n", a[2],a[3]);
	}
	else
	{
		printf("-1");
	}
}
