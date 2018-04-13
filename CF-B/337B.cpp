#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a%b);
}

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    if (a*d == b*c) cout << "0/1";
    else if (a*d > b*c) {
        int m = a*d-b*c;
        int n = a*d;
        int p = gcd(m, n);
        m/=p;
        n/=p;
        cout << m << "/" << n;
    } else {
        int m = b*c-a*d;
        int n = b*c;
        int p = gcd(m, n);
        m/=p;
        n/=p;
        cout << m << "/" << n;
    }
    
    return 0;
}
