#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<bool> s(100005, true);

void sieve() {
    s[0] = s[1] = false;
    for (int i = 2; i*i <= 100005 ; i++) {
        if (s[i]) {
            for (int j = i*2; j < 100005; j+= i) {
                s[j] = false;
            }
        }
    }
}

int findp(int x) {
    int u = x;
    while (!s[u]) u++;
    return u-x;
}

int main(int argc, char const* argv[]) {
    int m, n;
    cin >> m >> n;
    sieve();
    vector<vector<int> > v(m, vector<int>(n));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> v[i][j];
        }
    }


    int res = 1e9;
    for (int i = 0; i < m; i++) {
        int cnt = 0;
        for (int j = 0; j < n; j++) {
            cnt += findp(v[i][j]);
        }
        res = min(res, cnt);
    }
    for (int j = 0; j < n; j++) {
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            cnt += findp(v[i][j]);
        }
        res = min(res, cnt);
    }
    cout << res;
    return 0;
}
