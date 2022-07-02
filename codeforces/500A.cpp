#include <bits/stdc++.h>

using namespace std;

void dfs(vector<vector<int> >& v, vector<bool>& visited, int x) {
    if (visited[x]) return;
    visited[x] = true;
    for (int next : v[x]) {
        dfs(v, visited, next);
    }
}

int main(int argc, char const *argv[])
{
    int n, t;
    cin >>n >> t;
    vector<vector<int> > v(n+1);
    vector<bool> visited(n+1, false);
    for (int i = 1; i < n; i++) {
        int x;
        cin >> x;
        v[i].push_back(x+i);
    }
    dfs(v, visited, 1);
    if (visited[t]) cout << "YES";
    else cout << "NO";
    return 0;
}
