#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, d;
    cin >> n >> d;
    vector<pair<int, int>> v(n);
    for (int i = 0; i < n; i++) {
        int m, s;
        cin >> m >> s;
        v[i] = make_pair(m, s);
    }
    sort(v.begin(), v.end());
    int l = 0;
    unsigned long long res = 0;
    unsigned long long sum = 0;
    for (int  r = 0; r < v.size(); r++) {
        sum += v[r].second;
        while (v[l].first + d <= v[r].first) {
            sum -= v[l].second;
            l++;
        }
        res = max(sum, res);
    }
    cout << res;

    return 0;
}
