#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int path;
long long res = 1;
vector<int> a[51];
bool visited[51] = {false};

void dfs(int p) {
    if (visited[p]) return;
    visited[p] = true;
    path++;
    if (path > 1) res *= 2;
    for (int i = 0; i < a[p].size(); i++) {
        dfs(a[p][i]);
    }
}


int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        a[x].push_back(y);
        a[y].push_back(x);
    }

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            path = 0;
            dfs(i);
        }
    }
    cout << res;
    return 0;
}
