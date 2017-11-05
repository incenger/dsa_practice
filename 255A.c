#include <stdio.h>

int main(void) {
	
	int n;
	int day[20];
	int chest =0;
	int biceps = 0;
	int back = 0;
	scanf("%d", &n);
	for (int i = 0; i<n; i++)
	{
		scanf("%d", &day[i]);
	}
	for (int i = 0; i <n; i++)
	{
		if (i % 3 == 0)
		{
			chest += day[i];
		}
		else if (i% 3 == 1)
		{
			biceps += day[i];
		}
		else
		{
			back += day[i];
		}
	}
	if (chest > biceps)
	{
		if (chest > back)
		{
			printf("chest");
		}
		else 
		{
			printf("back");
		}
	}
	else
	{
		if(biceps > back)
		{
			printf("biceps");
		}
		else
		{
			printf("back");
		}
	}
}
