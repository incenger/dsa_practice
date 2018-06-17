#include <iostream>
#include <bits/stdc++.h>

using namespace std;

long long code(int v, int k) {
    long long res = 0;
    long long reduc = 1;
    while (v / reduc) {
        res += v/reduc;
        reduc*=k;
    }
    return res;
}

int main(int argc, char const* argv[]) {
    int n, k;
    cin >> n >> k;
    int lo = 1;
    int hi = n;
    while (lo < hi) {
        int mi = (lo + hi)/2;
        if (code(mi, k) >= n) hi = mi;
        else lo = mi +1;
    }
    cout << lo;
    return 0;
}