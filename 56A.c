#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void) {
	// your code goes here
	int n;
	char alcohol[11][11];
	strcpy(alcohol[0], "ABSINTH");
	strcpy(alcohol[1], "BEER");
	strcpy(alcohol[2], "BRANDY");
	strcpy(alcohol[3], "CHAMPAGNE");
	strcpy(alcohol[4], "GIN");
	strcpy(alcohol[5], "RUM");
	strcpy(alcohol[6], "TEQUILA");
	strcpy(alcohol[7], "SAKE");
	strcpy(alcohol[8], "VODKA");
	strcpy(alcohol[9], "WHISKEY");
	strcpy(alcohol[10], "WINE");
	scanf("%d", &n);
	char client [100][101];
	int temp;
	int count =0;
	for (int i =0; i < n; i++)
	{
		scanf("%s", client[i]);
	}
	for (int i = 0; i< n; i++)
	{
		if (!(isalpha(client[i][0])))
		{
			temp = atoi(client[i]);
			if (temp < 18)
			{
				count++;
			}
		}
		else
		{
			for (int j = 0; j < 11; j++)
			{
				if (strcmp(client[i], alcohol[j]) == 0)
				{
					count++;
				}
			}
		}
	}
	printf("%d", count);
	
}
