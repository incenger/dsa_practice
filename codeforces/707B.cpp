#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<pair<int, int> > > v(n+1);
    vector<bool> bakery(n+1, false);
    for (int i = 0; i < m; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        v[x].push_back(make_pair(y, z));
        v[y].push_back(make_pair(x, z));
    }
    for (int i = 0; i < k; i++) {
        int x;
        cin >> x;
        bakery[x] = true;
    }
    int ans = -1;
    for (int i = 1; i <= n; i++) {
        if (!bakery[i]) continue;
        for (int j = 0; j < v[i].size(); j++) {
            if (bakery[v[i][j].first]) continue;
            if (ans == -1) ans = v[i][j].second;
            else if (ans > v[i][j].second) ans =  v[i][j].second;
        }
    }
    cout << ans;
    return 0;
}
