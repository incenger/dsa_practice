#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n+1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
        v[i] += v[i-1];
    }
    int m;
    cin >> m;
    while (m--) {
        int x;
        cin >> x;
        int lo = 1;
        int hi = n;
        while (lo < hi) {
            int mid = (lo+hi)/2;
            if (x > v[mid]) lo = mid +1;
            else hi = mid;
        }
        cout << lo << endl;
    }
    return 0;
}
