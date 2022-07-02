#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const* argv[]) {
    int n, k;
    cin >> n >> k;
    vector<long long> v(n);
    map<long long, long long > left, right;
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        right[v[i]]++;
    }
    long long res = 0;
    for (int i = 0; i < n; i++) {
        right[v[i]]--;
        long long r = right[v[i]*k];
        long long l = left[v[i]/k]*(v[i] % k == 0);
        // cout << r << " " << l << " " << right[v[i]] << " " << left[v[i]] << endl;
        left[v[i]]++;
        res += r*l;
    }
    cout << res;

    return 0;
}
