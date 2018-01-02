#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int sol(vector<long long> &a, int n, int c) {
	auto mi = *min_element(a.begin(), a.end());
	auto ma = *max_element(a.begin(), a.end());
	long long lo = 1;
	long long hi = ma - mi;
	while (lo < hi) {
		long long mi = lo + (hi - lo+1)/2;
		int cow = 1;
		long long current = a[0];
		for (int i = 1; i < n; i++) {
			if (a[i] - current >= mi) {
				++cow;
				current = a[i];
			}
		}
		if (cow < c) hi = mi-1;
		else lo = mi;
	}
	return lo;
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n, c;
		cin >> n >> c;
		vector<long long> a;
		for (int i = 0; i < n; i++) {
			long long x;
			cin >> x;
			a.push_back(x);
		}
		sort(a.begin(), a.end());
		cout << sol(a, n, c) << endl;
	}
	return 0;
}