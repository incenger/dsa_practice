#include <iostream>
#include <bits/stdc++.h>
#include <set>
using namespace std;

int main() {
	vector<string> c;
	int n, m;
	cin >> n >> m;
	set<int> dis;
	for (int i =0; i < n ; i++) {
		string s;
		cin >> s;
		c.push_back(s);
	}
	bool sol = true;
	for (int i =0; i < n ; i++) {
		int candy = 0, dwarf = 0;
		for (int j =0; j < m ; j++) {
			if(c[i][j] == 'S') candy = j;
			if(c[i][j] == 'G') dwarf = j;
		}
		if (candy < dwarf) {
			sol = false;
			break;
		}
		dis.insert(candy - dwarf);
	}
	if (sol) cout << dis.size();
	else cout << -1;
	return 0;
}	