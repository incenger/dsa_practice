#include <stdio.h>

int main(void) {
	// count the number of postive, negative and 0 in array
	// 0 must be in thrid set
	// first set must cointain odd number of negatives
	// second set must cointain odd number of negatives
	int n;
	scanf("%d", &n);
	int number[100];
	int neg[100];
	int neg_count = 0;
	int pos[100];
	int pos_count = 0;
	int zero[100];
	int zero_count = 0;
	for (int i = 0; i< n; i++)
	{
		scanf("%d", &number[i]);
		if(number[i] > 0)
		{
			pos[pos_count] = number[i];
			pos_count++;
		}
		else if (number[i] < 0) 
		{
			neg[neg_count] = number[i];
			neg_count++;
		}
		else
		{
			zero[zero_count] = number[i];
			zero_count++;
		}
	}
	if (neg_count % 2 == 1)
	{
		printf("1 %d\n", neg[0]);
		printf("%d ", pos_count + neg_count -1);
		for (int i = 1; i < neg_count; i++)
		{
			printf("%d ", neg[i]);
		}
		for (int i =  0; i < pos_count; i++)
		{
			printf("%d ", pos[i]);
		}
		printf("\n");
		printf("%d ", zero_count);
		for (int i =0; i < zero_count; i++)
		{
			printf("0 ");
		}
	}
	else 
	{
		printf("1 %d\n", neg[0]);
		printf("%d ", pos_count + neg_count -2);
		for (int i = 2; i < neg_count; i++)
		{
			printf("%d ", neg[i]);
		}
		for (int i =  0; i < pos_count; i++)
		{
			printf("%d ", pos[i]);
		}
		printf("\n");
		printf("%d ", zero_count + 1);
		for (int i =0; i < zero_count; i++)
		{
			printf("0 ");
		}
		printf("%d", neg[1]);
	}
	
	
	
}
