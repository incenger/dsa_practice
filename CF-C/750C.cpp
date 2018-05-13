#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n;
    cin >> n;

    int INF = (int) 1e9;
    int low = -INF;
    int high = INF;
    int del = 0;

    for (int i = 0; i < n; i++) {
        int c, d;
        cin >> c>> d;
        if (d == 1) low = max(1900-del, low);
        else high = min(1899-del, high);
        del += c;
    }
    if (low > high) cout << "Impossible";
    else if (high > INF/2) cout << "Infinity";
    else cout << high + del;
    return 0;
}
