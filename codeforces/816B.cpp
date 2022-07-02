#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n, k, q;
    cin >> n >> k >> q;
    vector<int> v(200002, 0);
    for (int i = 0; i < n; i++) {
        int l, r;
        cin >> l >> r;
        v[l]++;
        v[r+1]--;
    }
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) v[i] += v[i-1];
    }

    for (int i = 0; i < v.size(); i++) {
        if (v[i] >= k) v[i] = 1;
        else v[i] = 0;
    }
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) v[i] += v[i-1];
    }
    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        cout << v[r] - v[l-1] << endl;
    }

    
    return 0;
}
