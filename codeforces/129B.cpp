#include <iostream>
#include <bits/stdc++.h>
#include <set>

using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	vector<int> degree(n+1, 0);
	set< pair<int,int> > edge;
	for (int i = 0; i < m ; i++) {
		int x, y;
		cin >> x >> y;
		degree[x]++;
		degree[y]++;
		edge.insert(make_pair(x, y));
	}
	int res = 0;
	
	while(!edge.empty()) {
		vector<int> edgeRemove;
		for (int i = 1; i <= n; i++) {
			if(degree[i] == 1) {
				edgeRemove.push_back(i);
			}
		}
		int count = edgeRemove.size();
		if (count  > 0) res++;
		else break;
		for (int i = 0; i < count; i++) {
			set<pair<int, int>>::iterator it;
			for (it = edge.begin(); it!= edge.end(); it++) {
				if(it->first == edgeRemove[i] || it->second == edgeRemove[i]) {
					degree[it->first]--;
					degree[it->second]--;
					edge.erase(it);
					break;
				}
			}
		}
	}
	cout << res;
	return 0;
}