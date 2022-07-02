#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int lo = 0;
    int hi = n;
    while (lo < hi) {
        int res = (lo +hi+1)/2;
        int t = 5*res*(res+1)/2 + k;
        if (t > 240) hi = res-1;
        else lo = res;
    }
    cout << lo;
    return 0;
}
