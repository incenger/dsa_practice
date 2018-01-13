#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int p, q, l, r;
	cin >> p >> q >> l >> r;
	bool moment[r-l+1] = {false};
	vector<pair<int, int>> z, x;
	while(p--) {
		int a, b;
		cin >> a >> b;
		z.push_back(make_pair(a, b));
	}
	
	while(q--) {
		int c, d;
		cin >> c >> d;
		x.push_back(make_pair(c, d));
	}
	for (int i = 0; i < z.size(); i++) {
		for (int j = 0; j < x.size(); j++) {
			int lower = z[i].first - x[j].second;
			int upper = z[i].second - x[j].first;
			if (lower <= upper ) {
				for (int k = l; k<= r; k++) {
					if (lower <= k && k <= upper) moment[k-l] = true;
				}
			}
		}
	}
	int res = 0;
	for (int i = 0; i < r -l +1; i++) {
		if (moment[i]) res++;
	}
	cout << res;
	return 0;
}