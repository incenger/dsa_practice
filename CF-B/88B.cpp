#include <iostream>
#include <bits/stdc++.h>
#include <stdio.h>
#include <ctype.h>
#include <cmath>

using namespace std;

int main() {
	int n, m, x;
	cin >> n >> m >> x;
	x *= x;
	char a[30][30];
	bool key[26] = {false};
	bool used[26] = {false};
	
	vector< pair<int, int> > s;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
			if (a[i][j] != 'S') key[a[i][j] - 'a'] = true;
			else s.push_back(make_pair(i, j));
		}
	}
	bool shift = !s.empty();
	
	for (int i = 0; i < s.size(); i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				if (a[j][k] != 'S') {
					double dis = pow(s[i].first - j, 2) + pow(s[i].second - k, 2);
					if (dis <= x) used[a[j][k] - 'a'] = true;
				}
			}
		}
	}
	
	int q;
	cin >> q;
	string text;
	cin >> text;
	int hands = 0;
	for (int i =0; i < q; i++) {
		char c = text[i];
		if(islower(c)) {
			if (!key[c - 'a']) {
				cout << -1;
				return 0;
			}
		} else {
			if (!key[c - 'A'] || !shift) {
				cout << -1;
				return 0;
			} else if (!used[c - 'A']) hands++;
		}
	}
	cout << hands;
	return 0;
}