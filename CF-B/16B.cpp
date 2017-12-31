#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	vector< pair<int,int> > v;
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		v.push_back( make_pair(y, x));
	}
	sort(v.begin(), v.end());
	int matches = 0;
	int i = m -1;
	while (n > 0 && i>= 0) {
		if (n >= v[i].second) {
			n -= v[i].second;
			matches += v[i].first*v[i].second;
		} else {
			matches += v[i].first*n;
			n = 0;
		}
		i--;
	} 
	cout << matches;
	return 0;
}