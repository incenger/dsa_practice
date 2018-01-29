#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, x0, y0;
    cin >> n >> x0 >> y0;
    bool horizontal = false;
    set<double> slope;
    while(n--) {
        int x, y;
        cin >> x >> y;
        if (x == x0) horizontal = true;
        else {
            double s = 1.0*(y-y0)/(x-x0);
            slope.insert(s);
        }
    }
    if (horizontal) cout << slope.size() + 1 << endl;
    else cout << slope.size() << endl;
    return 0;
}
