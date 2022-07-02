#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n, a, b;
    cin >> n >> a >> b;
    int lo = 1;
    int hi = min(a, b);
    while (lo < hi) {
        int mi = (lo +hi +1)/2;
        if (a/mi + b/mi >= n) lo = mi;
        else hi = mi -1;
    }
    cout << lo;
    return 0;
}
