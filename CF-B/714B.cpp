#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
using namespace std;

int main() {
	set<int> a;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		a.insert(x);
	}
	if (a.size() > 3) cout << "NO";
	else if (a.size() < 3) cout <<  "YES";
	else {
		vector<int> x;
		set<int>::iterator it;
		for (it = a.begin(); it != a.end(); it++) {
			x.push_back(*it);
		}
		if (abs(x[1] - x[0]) == abs(x[2] - x[1])) cout << "YES";
		else cout << "NO";
	}
	return 0;
}