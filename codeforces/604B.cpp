#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n, k;
    cin >> n >> k;
    vector<long long> v(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    long long lo = v[n-1];
    long long hi = accumulate(v.begin(), v.end(), 0LL);
    while (lo < hi) {
        long long mi = lo + (hi-lo)/2;
        int cnt = 0;
        long long x = 0, y = n-1;
        // cout << lo <<" "<< hi << " " << mi << endl;
        while (x <= y) {
            if (v[y] + v[x] <= mi) {
                x++;
                y--;
            } else y--;
            // else if (w + v[x] <= mi) w+= v[x++];
            cnt++;
            // cout << x << " " << y << " "<<  w << " " << cnt << endl;
        }
        // cout << cnt << endl;
        if (cnt > k) lo = mi +1;
        else hi = mi;
    }
    cout << lo;
    return 0;
}
