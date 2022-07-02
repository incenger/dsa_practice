#include <iostream>
#include <bits/stdc++.h>

#define MAX 1001000
#define MOD 1073741824

using namespace std;

int main() {
    int d[MAX];
    int a, b, c;
    cin >> a >> b >> c;
    for (int i = 1; i <= a*b*c; i++)
        for (int j = i; j <= a*b*c; j += i)
            d[j]++;

    unsigned long long res = 0;
    for (int i = 1; i <= a; i++) {
        for (int ii = 1; ii <= b; ii++) {
            for (int iii = 1; iii <= c; iii++) {
                res = (res +d[i*ii*iii])%MOD;
            }
        }
    }
    cout << res % MOD << endl;
    return 0;
}
