#include <iostream>
#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

int main() {
	vector<pair<double, int>> m;
	int n,t1, t2, k;
	cin >> n >> t1 >> t2 >> k;
	for (int i = 0; i < n; i++) {
		int v1, v2;
		cin >> v1 >> v2;
		double h1 = 1.0*v1*t1*(100 -k)/100 + v2*t2;
		double h2 = 1.0*v2*t1*(100- k)/100 + v1*t2;
		m.push_back(make_pair(max(h1, h2), -(i+1)));
	}
	sort(m.begin(), m.end());
	for (int i = n-1; i >= 0; i--) {
		cout << -m[i].second << " " << setprecision(2) << fixed << m[i].first << endl;
	}
	return 0;
}