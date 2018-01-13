#include <iostream>
#include <bits/stdc++.h>
#define MAX 1000000000
using namespace std;

int n, m, xc, yc;
vector<pair<int, int>> direction;

bool valid(long long x, long long y) {
	return (0 < x && x <= n) && (0 < y && y <= m);
}

long long move(int i) {
	int dx = direction[i].first;
	int dy = direction[i].second;
	long long hi  = MAX;
	long long lo = 0;
	while (lo < hi) {
		long long mi = lo + (hi -lo + 1)/2;
		if( valid(xc + dx*mi , yc + dy*mi) ) {
			lo = mi;
		} else {
			hi = mi -1;
		}
	}
	xc += dx*lo;
	yc += dy*lo;
	return lo;
}


int main() {
	cin >> n >> m >> xc >> yc;
	int k;
	cin >> k;
	long long res = 0;
	for (int i = 0; i < k; i++) {
		int dx, dy;
		cin >> dx >> dy;
		direction.push_back(make_pair(dx, dy));
	}
	for (int i = 0; i < k; i++) {
		res += move(i);
	}
	cout << res;
	
	return 0;
}