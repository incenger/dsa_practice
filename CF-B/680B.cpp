#include <iostream>
using namespace std;

int main() {
	int n, a;
	cin >> n >> a;
	int t[100];
	for (int i = 0; i < n; i++) cin >> t[i];
	a--;
	int cri = 0;
	int dis = 0;
	if (t[a] == 1) cri++;
	dis++;
	while (a + dis < n || a - dis >= 0) {
		if (a + dis < n && a - dis >= 0) {
			if (t[a+dis] && t[a-dis]) cri += 2;
		}
		else if (a + dis < n) cri += t[a+dis];
		else cri += t[a-dis];
		dis++;
	}
	cout << cri;
	return 0;
}