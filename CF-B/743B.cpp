#include <iostream>
#include <bits/stdc++.h>

using namespace std;

long long power2(int n) {
    long long res = 1;
    for (int i = 0; i < n; i++) {
        res *= 2;
    }
    return res;
}

int sol(int n, long long k) {
    if (n == 1) return 1;
    long long index = k % power2(n-1);
    if (index == 0) return n;
    else return sol(n-1, index);
}

int main(int argc, char const* argv[]) {
    int n;
    long long k;
    cin >> n >> k;
    cout << sol(n, k);
    return 0;
}
