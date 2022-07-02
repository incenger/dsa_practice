#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k, l, r, sall, sk;
    int a[1000];
    cin >> n >> k >> l >> r >> sall >> sk;
    int s = sk/k;
    int remain = sk % k;
    for (int i = 0; i < k; i++) {
        if (remain > 0) a[i] = s + 1;
        else a[i] = s;
        remain--;
    }
    int left = n - k;
    if (left > 0) {
        s = (sall - sk)/left;
        remain = (sall - sk) % left;
        for (int i = k ; i < n; i++) {
            if (remain > 0) a[i] = s +1;
            else a[i] = s;
            remain--;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    return 0;
}
