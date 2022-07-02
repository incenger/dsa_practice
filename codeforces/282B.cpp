#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> g(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> g[i];
    }

    long long sA = accumulate(a.begin(), a.end(), 0LL);
    int cnt = 0;
    while (abs(1000*cnt - sA) > 500) cnt++;
    if (cnt > n) cout << -1;
    else {
        for (int  i = 0;  i < cnt; i++) cout << "G";
        for (int  i = cnt; i < n; i++) cout << "A";
    }
    return 0;
}
