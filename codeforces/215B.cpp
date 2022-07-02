#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
	int n, m, k;
	cin >> n;
	int r1[n];
	for (int i = 0; i < n; i++) cin >> r1[i];
	cin >> m;
	int p1[m];
	for (int i = 0; i < m; i++) cin >> p1[i];
	cin >> k;
	int p2[k];
	for (int i = 0; i < k; i++) cin >> p2[i];
	int a, b;
	cin >> a >> b;
	int r = *max_element(r1, r1 + n);
	int p = *min_element(p2, p2 + k);
	double res = 0;
	for (int i = 0; i < m; i++) {
		double radius = r*sqrt(1.0*(b*p1[i])/(p*a + p1[i]*b));
		if (radius > res) res = radius;
	}
	cout <<setprecision(12) << fixed << res;
	return 0;
}