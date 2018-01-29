#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    int a[100000];
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    long long res = 0;
    int breakPoint = -1;
    for (int i = 0; i < n -1; i++) {
        if (a[i] < 0 && a[i+1] >= 0) {
            breakPoint = i;
        }
    }

    for (int i = 0; i < n; i++) {
        if (a[i] < 0 && k > 0) {
            a[i] = -a[i];
            k--;
        }
    }

   
    if (breakPoint == -1) {
        if (k % 2 == 1 ) {
            a[0] = -a[0];
        }
    } else {
        if (k > 0) {
            if (k % 2 == 1) {
                if (a[breakPoint] < a[breakPoint+1]) a[breakPoint] = -a[breakPoint];
                else a[breakPoint+1] = -a[breakPoint+1];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        res += a[i];
    }
    cout << res;
    return 0;
}
