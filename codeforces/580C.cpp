#include <bits/stdc++.h>

using namespace std;

int ans = 0;

void dfs(vector<vector<int> >& v, vector<bool>& cat, int parent, int x, int cnt, int ma) {
    
    if (cat[x]) cnt++;
    else cnt = 0;
    if (cnt > ma) return;
    bool f = false;
    for (int next : v[x]) {
        if (next != parent) {
            dfs(v, cat, x, next, cnt, ma);
            f = true;
        }
    }
    if (!f) ans++;
}


int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n >> m;
    vector<bool> cat(n+1, false);
    for (int i = 1; i <= n ; i++) {
        int x;
        cin >> x;
        if (x == 1) cat[i] = true;
    }
    vector<vector<int> > v(n+1);
    for (int i = 1; i < n; i++) {
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    dfs(v, cat, 0, 1, 0, m);
    cout << ans;
    return 0;
}
