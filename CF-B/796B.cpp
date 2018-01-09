#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	bool hole[1000005] = {false};
	int n, m, k;
	scanf("%d %d %d", &n, &m, &k);
	for (int i = 0; i < m; i++) {
		int x;
		cin >> x;
		hole[x] = true;
	}
	
	bool fall = hole[1];
	int bone = 1;
	while (k--) {
		int u,v;
		scanf("%d %d", &u, &v);
		if (fall) break;
		if (bone == u) bone = v;
		else if (bone == v) bone = u;
		fall = hole[bone];
	}
	cout << bone;
	return 0;
}