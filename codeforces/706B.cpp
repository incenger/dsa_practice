#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n;
    cin >> n;
    vector<int> v(n+1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    int m;
    cin >> m;
    while (m--) {
        int x;
        cin >> x;
        int lo = 0;
        int hi = n;
        while (lo < hi) {
            int mi = (lo +hi+1)/2;
            if (x < v[mi]) hi = mi -1;
            else lo = mi;
        }
        cout <<  lo << endl;
    }
    
    return 0;
}
