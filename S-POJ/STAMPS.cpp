#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int need, friends;
		cin >> need >> friends;
		vector<int> a;
		for (int j = 0; j < friends; j++) {
			int x;
			cin >> x;
			a.push_back(x);
		}
		sort(a.begin(), a.end());
		int have = 0, borrow = 0;
		for (int j = friends - 1; j > 0; j--) {
			borrow++;
			have += a[j];
			if (have >= need) break;
			
		}
		cout << "Scenario #" << i <<":" << endl;
		if (have >= need) cout << borrow << endl;
		else cout << "impossible" << endl;
		cout << endl;
	}
	return 0;
}