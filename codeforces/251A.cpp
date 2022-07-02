#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n, d;
    cin >> n >> d;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    unsigned long long res = 0;
    sort(v.begin(), v.end());
    for (auto it = v.begin(); it!= v.end(); it++) {
        int cnt = upper_bound(it, v.end(), static_cast<long long>(*it) + d) - it - 1;
        res += static_cast<long long>(cnt)*(cnt-1)/2;
    }
    cout << res;
    return 0;
}
