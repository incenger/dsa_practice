#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n, t;
    cin >> n >> t;
    vector<long long> v(n+1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    for (int i = 1; i <= n; i++) {
        v[i] += v[i-1];
    }

    int res = 0;
    for (auto it = v.begin(); it != v.end(); it++) {
        int x = upper_bound(it, v.end(), *it + t) - it -1;
        res = max(x, res);

    }
    cout << res;
    return 0;
}
