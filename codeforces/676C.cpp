#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int sol(vector<int> &v, char x, int k) {
    int res = 0;
    for (int i = 1; i <= v.size(); i++) {
        int lo = i;
        int hi = v.size()-1;
        while (lo < hi) {
            int mi = (lo + hi+1)/2;
            // cout << i << " " << lo << " " << hi << " " << mi << endl;
            if (v[mi]-v[i-1] <= k) {
                lo = mi;
            } else {
                hi = mi -1;
            }
        }
        res = max(res, lo - i +1);
    }
    return res;
}

int main(int argc, char const* argv[]) {
    int n,k;
    cin >> n >> k;
    string s;
    cin >> s;
    vector<int> a(n+1, 0);
    vector<int> b(n+1, 0);
    for (int i = 0; i < n; i++) {
        a[i+1] = a[i] + (s[i] == 'a');
        b[i+1] = b[i] + (s[i] == 'b');
    }
    cout << max(sol(a, 'a', k), sol(b, 'b', k));
    return 0;
}
