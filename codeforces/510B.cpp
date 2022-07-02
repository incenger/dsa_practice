#include <iostream>
#include <bits/stdc++.h>

using namespace std;

char a[50][50];
int m, n;
bool cycle = false;
bool visited[50][50];

bool isValid(int i , int j) {
    return (0 <= i && i < m && 0 <= j && j < n);
}

void dfs(int i, int j, int u, int v) {
    // go back to the previous cell
    if (visited[i][j]) {
        cycle = true;
        return;
    }
    visited[i][j] = true;
    if (isValid(i+1, j) && a[i+1][j] == a[i][j] && ((i+1 != u) || (j!= v))) dfs(i+1, j, i, j);
    if (isValid(i-1, j) && a[i-1][j] == a[i][j] && ((i-1 != u) || (j!= v))) dfs(i-1, j, i, j);
    if (isValid(i, j+1) && a[i][j+1] == a[i][j] && ((i != u) || (j+1!= v))) dfs(i, j+1, i, j);
    if (isValid(i, j-1) && a[i][j-1] == a[i][j] && ((i != u) || (j-1!= v))) dfs(i, j-1, i, j);
}

int main() {
    cin >> m >> n;
    memset(visited, false, sizeof(visited));
    for (int  i = 0; i < m; i++)
        for (int  j = 0; j < n; j++)
            cin >> a[i][j];
    for (int  i = 0; i < m; i++)
        for (int  j = 0; j < n; j++)
            if (!visited[i][j]) dfs(i, j, -1, -1);

    if (cycle) cout << "Yes";
    else       cout << "No";
    return 0;
}
