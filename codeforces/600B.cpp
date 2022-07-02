#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n, m;
    cin >> n >> m;
    vector<int> a(n, 0);
    vector<int> b(m, 0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
    sort(a.begin(), a.end());
    for (int i = 0; i < m; i++) {
        cout << upper_bound(a.begin(), a.end(), b[i]) - a.begin();
        if (i != m-1) cout << " ";
    }
    return 0;
}
