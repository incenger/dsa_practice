#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
#define oo 10000000

using namespace std;

int main() {
    int a[15];
    int n, l, r, x;
    cin >> n >> l >> r >> x;
    for (int i = 0; i < n; i++) cin >> a[i];
    int res = 0;
    int subset = 1 << n;
    for (int i = 0; i < subset; i++) {
        int easy = oo, hard = 0, sum = 0, cnt = 0;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                cnt++;
                sum += a[j];
                easy = min(easy, a[j]);
                hard = max(hard, a[j]);
            }
        }
        if (l <= sum && sum <= r && hard-easy >= x && cnt > 1) res++;
    }
    cout << res;
    return 0;
}

