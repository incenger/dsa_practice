#include <iostream>
#include <bits/stdc++.h>
#include <string.h>

using namespace std;

long long edge, vertex;

vector<int> a[150001];
bool visited[150001];

void dfs(int v) {
    vertex++;
    visited[v] = true;
    for (int i = 0; i < a[v].size(); i++) {
        edge++;
        if (!visited[a[v][i]]) dfs(a[v][i]);
    }
}

int main() {
    int n, m;
    memset(visited, false, 150001);
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        a[x].push_back(y);
        a[y].push_back(x);
    }

    bool res = true;

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            edge = 0;
            vertex = 0;
            dfs(i);
            if (edge != vertex*(vertex-1)) {
                res = false;
                break;
            }
        }
    }

    if (res) cout << "YES";
    else cout << "NO";
    return 0;
}
