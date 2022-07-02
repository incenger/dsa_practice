#include <bits/stdc++.h>

using namespace std;

void dfs(vector<vector<int> >& v, vector<bool>& visited, int x) {
    visited[x]  = true;
    for (int next : v[x]) if (!visited[next]) dfs(v, visited, next);
}


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    vector<vector<int> > v(n+1);
    vector<int> x(n+1);
    vector<int> y(n+1);
    vector<bool> visited(n+1, false);
    for (int  i = 1; i <= n; i++) {
        cin >> x[i] >> y[i];
        for (int  j = 1; j < i; j++) {
            if (x[j] == x[i] || y[j] == y[i]) {
                v[i].push_back(j);
                v[j].push_back(i);
            }
        }
    }
    int cnt = 0;
    for (int  i = 1; i <= n; i++) {
        if (!visited[i]) { 
            dfs(v, visited, i);
            cnt++;
        }
    }
    cout << cnt-1;
    return 0;
}
