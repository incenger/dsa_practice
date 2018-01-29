#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int res = 0;
    while (m > n) {
        if (m % 2 ==0 ) m/= 2;
        else  m += 1;
        res++;
    }
    res += (n-m);
    cout << res;
    return 0;
}
