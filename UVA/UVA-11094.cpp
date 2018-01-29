#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool visited[20][20];
char c[20][20];
char land;
int n, m;

int dfs(int i, int j) {
    if (i < 0 || i >= n) return 0;
    if (j < 0) j+= m;
    else if (j >= m) j-= m;
    if (visited[i][j]) return 0;
    if (c[i][j] != land) return 0;
    visited[i][j] = true;
    return 1 + dfs(i+1,j) +dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1);
}

int main() {
    while (cin >> n >> m) {
        memset(visited, false, sizeof(visited[0][0])*20*20);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> c[i][j];
            }
        }
        int x, y;
        cin >> x >> y;
        land = c[x][y];
        dfs(x, y);
        int res = 0;
        for (int i =0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && c[i][j] == land) {
                    int regions = dfs(i, j);
                    if (regions > res) res = regions;
                }
            }
        }
        cout << res << endl;
    }
    return 0;
}
