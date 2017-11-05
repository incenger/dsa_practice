#include <stdio.h>
//check if a in (b, c) or (c, b)
int inside(int a, int b, int c)
{
	if (b < a && a <c)
	{
		return 0;
	}
	else if (c < a && a <b)
	{
		return 0;
	}
	return 1;
}

int outside(int a, int b, int c)
{
	if (b < a && a >c)
	{
		return 0;
	}
	else if (c > a && a <b)
	{
		return 0;
	}
	return 1;
}


int cut (int a, int b, int c, int d)
{
	if (inside(a , c, d) == 0 && outside(b, c, d) == 0)
	{
		return 0;
	}
	else if (inside(b , c, d) == 0 && outside(a, c, d) == 0)
	{
		return 0;
	}
	return 1;
}

int main(void) {
	// if exist a[i] that  a[j]<a[i]<a[j+1] for i = 1..n-1 and a[i+1] > a[j+1] then the answer is yes
	int n;
	int a[1000];
	scanf("%d\n", &n);
	for (int i = 0; i <n; i++)
	{
		scanf("%d ", &a[i]);
	}
	for (int i = 0; i < n-1; i++ )
	{
		for (int j = 0; j < n-1; j++)
		{
			if (cut(a[i], a[i+1], a[j], a[j+1]) == 0)
			{
				printf("yes");
				return 0;
			}
		}
	}
	printf("no");
}
