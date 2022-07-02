#include <iostream>
#include <bits/stdc++.h>

using namespace std;

set<long long> tprime;

bool isPrime(int n) {
    if (n == 1) return false;
    for (int  i = 2; i*i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}



int main() {
    int n;
    cin >> n;
    tprime.insert(4);
    for (int i= 3; i <= 1000000; i+=2) {
        if (isPrime(i)) tprime.insert((long long)i*i);
    }
    while (n--) {
        long long x;
        cin >> x;
        if (tprime.find(x) == tprime.end()) cout << "NO"<< endl;
        else cout << "YES" << endl;
    }
    
    return 0;
}
