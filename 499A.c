#include <stdio.h>

int main(void) {
	int n;
	int x;
	scanf("%d %d", &n, &x);
	int l[50];
	int r[50];
	int init = 1;
	for (int i =0; i< n; i++)
	{
		scanf("%d %d", &l[i], &r[i]);
	}
	int j = 0;
	int minutes = 0;
	while ( j < n)
	{
		if ( (init +x) >  l[j] )
		{
			minutes = minutes + r[j] -init +1 ;
			init = r[j] +1;
			j++;
		}
		else if ( (init+x) <= l[j] )
		{
			init += x;
		}
	}
	printf("%d", minutes);
}
