#include <iostream>
#include <bits/stdc++.h>
char f[4][1000] = {"Grapes", "Carrots", "Kiwis", "Waste"};

using namespace std;

int main() {
	int n, m, k, t;
	cin >> n >> m >> k >> t;
	pair<int, int> w[1000];
	for (int i = 0; i < k; i++) {
		cin >> w[i].first >> w[i].second;
	}
	
	while (t--) {
		int r, c;
		cin >> r >> c;
		int num = 0;
		bool waste = false;
		for (int i = 0; i < k; i++) {
			if (w[i].first < r) num++;
			else if (w[i].first == r) {
				if (w[i].second < c) num++;
				else if (w[i].second == c) waste = true;
			}
		}
		int res;
		if (waste) res = 3;
		else {
			res = ( m*(r-1) + c - num) %3;
			
		}
		cout << f[res] << endl;
	}
	return 0;
}