#include <iostream>
#include <bits/stdc++.h>

using namespace std;

double calc(int n, double a, double b) {
    double res = 0;
    for (int i = 3; i <= n; i++) {
        res = 2*(a+1) -b;
        if (res < 0) return -1;
        b = a;
        a = res;
    }
    return res;
}

int main() {
    int n;
    double A;
    while(cin >> n >> A) {
        double hi = A, lo = 0, res = 0;
        for (int i = 0; i < 1000; i++) {
            double mid = (lo + hi)/2;
            if (calc(n, mid, A) >= 0) {
                res = calc(n, mid, A);
                hi = mid;
            } else lo = mid;
        }
        cout << fixed << setprecision(2) << res << endl; 
    }
    return 0;
}
