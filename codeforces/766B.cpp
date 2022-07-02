#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int a[100000];
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a+n);
	bool tri = false;
	for (int i = n-1; i >= 0; i--) {
		int c = a[i];
		int b = a[i-1];
		int j = i-2;
		while (j>= 0) {
			if (a[j] + b > c) {
				tri = true;
				break;
			} else j--;
		}
		if (tri) {
			cout << "YES";
			return 0;
		}
	}
	cout << "NO";
	return 0;
}