#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int numberOf1 = 0;
    unsigned long long res = 1;
    int prev = -1;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x == 1){
            numberOf1++;
            if (numberOf1 == 1) prev = i;
            else {
                res *= (i -prev);
                prev = i;
            }
        }
    }
    if (numberOf1 == 0) cout << 0 << endl;
    else cout << res;
    return 0;
}
