#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> diag1(1000*2+1, 0);
    vector<int> diag2(1000*2+1, 0);
    int n;
    cin >> n;
    while (n--) {
        int x, y;
        cin >> x >> y;
        diag1[x+y]++;
        diag2[1000 +(x-y)]++;
    }
    unsigned long long res = 0;
    for (auto &i : diag1) res += i*(i-1)/2;
    for (auto &i : diag2) res += i*(i-1)/2;
    cout << res;
    return 0;
}
