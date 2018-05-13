#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    auto r = v.begin() + n/2 -1;
    int cnt = 0;
    vector<bool> f(n, true);
    for (auto it = v.begin(); it != v.end(); it++) {
        if (!f[it-v.begin()]) continue;
        if (r == v.end()) break;
        r = lower_bound(r+1, v.end(), *it * 2);
        // cout << r-v.begin() << endl;
        if (r != v.end()) {
            cnt++;
            f[r - v.begin()] = false;
        }
    }
    cout << n - cnt;
    return 0;
}
