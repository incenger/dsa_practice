#include <stdio.h>
#include <string.h>

int main(void) {
	char a[4][103];
	scanf(" %s ", a[0]);
	scanf(" %s ", a[1]);
	scanf(" %s ", a[2]);
	scanf(" %s ", a[3]);
	int leng[4];
	int temp;
	for (int i =0; i < 4; i++)
	{
		leng[i] = strlen(a[i]) -2;
	}
	for (int i = 0; i <3;i++)
	{
		for (int j = 0; j < 3 -i; j++)
		{
			if (leng[j] > leng[j+1])
			{
				temp = leng[j];
				leng[j] = leng[j+1];
				leng[j+1] = temp;
			}
		}
	}
	int great = 0;
	if (leng[3] >= leng[2]*2)
	{
		great++;
	}
	if (leng[0] *2 <= leng[1])
	{
		great++;
	}
	if (great != 1)
	{
		printf("C");
		return 0;
	}
	else
	{
		if (leng[3] >= leng[2]*2)
		{
			for (int i = 0; i < 4; i++)
			{
				if (strlen(a[i]) -2 == leng[3])
				{
					printf("%c", a[i][0]);
					return 0;
				}
			}
		}
		if (leng[0] *2 <= leng[1])
		{
			for (int i = 0; i < 4; i++)
			{
				if (strlen(a[i]) -2 == leng[0])
				{
					printf("%c", a[i][0]);
					return 0;
				}
			}
		}
	}
}
