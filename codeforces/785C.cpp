#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool empty(unsigned long long n,unsigned long long m,unsigned long long d) {
    unsigned long long x = d - m -1;
    unsigned long long val = x*(x+1)/2;
    if (n  <= d + val) return true;
    else return false;
}

int main() {
    unsigned long long n, m;
    cin >> n >> m;
    if (m >= n) {
        cout << n;
    } else {
        unsigned long long lo = 0;
        unsigned long long hi = 2e9 ;
        n -= m;
        while (lo < hi) {
            unsigned long long mi = lo + (hi-lo)/2;
            unsigned long long val = mi*(mi-1)/2;
            if (n <= mi +val) hi  = mi;
            else lo = mi +1;
        }
        cout << lo + m;
    }
    return 0;
}
