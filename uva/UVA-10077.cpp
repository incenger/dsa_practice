#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct frac {
    int t;
    int b;
};

string path = "";

void binarySearch(frac q) {
    path = "";
    frac lo, hi;
    lo.t = 0;
    lo.b = 1;
    hi.t = 1;
    hi.b = 0;
    while (1.0*lo.t/lo.b < 1.0*hi.t/hi.b) {
        frac me;
        me.t = lo.t + hi.t;
        me.b = lo.b + hi.b;
        if (me.t == q.t && me.b == q.b) break;
        else if (1.0*me.t/me.b < 1.0*q.t/q.b) {
            lo = me;
            path += "R";
        }
        else {
            hi = me;
            path += "L";
        }
    }
}

int main() {
    while (true) {
        int x, y;
        cin >> x >> y;
        if (x == 1 && y == 1) break;
        frac q;
        q.t = x;
        q.b = y;
        binarySearch(q);
        cout << path << endl;
    }
    return 0;
}
