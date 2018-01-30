#include <iostream>
#include <bits/stdc++.h>
const unsigned long long MOD = 1000000007;

using namespace std;

long long powMOD(long long a, long long b) {
    if (b == 0) return 1 % MOD;
    if (b % 2 == 0)
        return (powMOD(a, b/2)*powMOD(a, b/2)) % MOD;
    else
        return a*(powMOD(a, b/2)*powMOD(a, b/2) % MOD) %MOD;
}

int main() {
    int n;
    cin >> n;
    cout << (powMOD(27,n) - powMOD(7, n) + MOD) % MOD;
    return 0;
}
