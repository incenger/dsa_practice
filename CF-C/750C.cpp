#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int check(long long ra, vector<int>& c, vector<int>& d) {
    for (int i = c.size()-1; i >= 0; i--) {
        ra -= c[i];
        if (ra >= 1900 && d[i] == 2) return 1;
        if (ra < 1900 && d[i] == 1) return -1;
    }
    return 0;
}

int main(int argc, char const* argv[]) {
    int n;
    cin >> n;

    vector<int> c(n), d(n);

    bool div2 = false;

    for (int i = 0; i < n; i++) {
        cin >> c[i] >> d[i];
        if (d[i] == 2) div2 = true;
    }

    if (!div2) {
        cout << "Infinity";
        return 0;
    }

    for (int i = 0; i < n -1 ; i++) {
        if (d[i] == 1 && d[i+1] == 2 && c[i] >= 0) {
            cout << "Impossible";
            return 0;
        }
        if (d[i] == 2 && d[i+1] == 1 && c[i] <= 0) {
            cout << "Impossible";
            return 0;
        }

    }

    long long max = 2e10;

    long long lo = -max;
    long long hi = max;
    while (lo < hi) {
        long long mi = lo + (hi-lo+1)/2;
        if (check(mi, c, d) == 0) { 
            lo = mi;
        }
        else if (check(mi, c, d) > 0) hi = mi-1;
        else lo = mi +1;
    }
    if(check(lo, c, d) != 0) cout << "Impossible";
    else if (lo == max) cout << "Infinity";
    else cout << lo;
    return 0;
}
