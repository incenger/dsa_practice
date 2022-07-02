#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a[101], d[101][3];
	memset(d, 0, sizeof(d[0][0])*3*101);
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}
	for (int i = 1; i <= n; i++) {
		if (a[i] == 1 || a[i] == 3) {
			d[i][1] = max(d[i-1][0] + 1, d[i-1][2] + 1);
		}
		if (a[i] == 2 || a[i] == 3) {
			d[i][2] = max(d[i-1][1] + 1, d[i-1][0] + 1);
		}
		d[i][0] = max(max(d[i-1][0], d[i-1][1]), d[i-1][2]);
	}
	int res = max(max(d[n][0], d[n][1]), d[n][2]);
	cout << n -  res;
	
	
	return 0;
}