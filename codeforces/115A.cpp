#include <bits/stdc++.h>

using namespace std;

void dfs(vector<set<int> >& v, vector<bool>& visited, int x, int c, int& m) {
    if (visited[x]) return;
    visited[x] = true;
    for (int next : v[x]) {
        dfs(v, visited, next, c+1, m);
        if (c+1 > m ) m = c+1;
    }
}


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    vector< set<int> > v(n+1);
    vector<bool> visited;
    for (int  i = 1; i <= n; i++) {
        int x;
        cin >> x;
        if (x != -1) {
            v[i].insert(x);
        }
    }
    int ma = 1;
    for(int  i = 1; i <=  n; i++) {
        visited = vector<bool>(n+1, false);
        dfs(v, visited, i, 1, ma);
    }
    cout << ma;
    return 0;
}
