#include <iostream>
#include <string.h>
using namespace std;

long long a[10000][10000];

long long cal(int n, int m) {
	if (a[n][m] != 0) return a[n][m];
	if (m == 0 || m == n) {
		a[n][m] = 1;
		return 1;
	}
	a[n][m] = cal(n-1, m) + cal(n-1, m-1);
	return a[n][m];
}

int main() {
	memset(a, 0, sizeof(a[0][0])*10000*10000);
	int n, m;
	while(true) {
		cin >> n >> m;
		if (n == 0 && m == 0) break;
		printf("%d things taken %d at a time is %lld exactly.\n", n, m, cal(n, m));
	}
	return 0;
}