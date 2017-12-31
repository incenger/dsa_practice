#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

vector<vector<int>> vii(101);
bool marked[101];
int n, m, count;
bool cycle;
int rem = 0;

//using adjacent list for graph
void gen() {
	memset(marked, 0, 101);
	cin >> n >> m;
	for (int i = 1; i <= m; i++) {
		int x, y;
		cin >> x >> y;
		vii[x].push_back(y);
		vii[y].push_back(x);
	}
}

void dfs(int u, int v) {
	marked[u] = true;
	count++; //count the length of the path
	for (int i = 0; i < vii[u].size(); i++) {
		if (!marked[vii[u][i]]) {
			dfs(vii[u][i], u);
		} else if (vii[u][i] != v) cycle = true; //if not return to its parent, the path is a cycle
	}
}

void team() {
	for (int i = 1; i<= n; i++) {
		if(!marked[i]) {
			count = 0;
			cycle = false;
			dfs(i, i);
			if (count % 2 == 1 && cycle) rem++;
		}
	}
}


int main() {
	gen();
	team();
	//if after removing the number of players is odd, we remove one more player
	if ((n - rem) % 2 == 0) cout << rem << endl;
	else cout << rem +1 << endl;
	return 0;
}