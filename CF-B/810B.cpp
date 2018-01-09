#include <iostream>
#include <bits/stdc++.h>
#define MAX 100000
using namespace std;

int main() {
	int n, j;
	cin >> n >> j;
	pair<long long, long long> p[MAX], dis[MAX];
	for (int i = 0; i < n; i++) {
		cin >> p[i].first >> p[i].second;
		dis[i].first = min(p[i].first, p[i].second - p[i].first);
		dis[i].second = i;
	}
	sort(dis, dis + n, greater<pair<long, long>>());
	for (int i = 0; i < j; i++) {
		p[dis[i].second].first *= 2;
	}
	long long res = 0;
	for (int i = 0; i < n; i++) {
		res += min(p[i].first, p[i].second);
	}
	cout << res;
	return 0;
}