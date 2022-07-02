#include <iostream>
#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

struct line {
    double A;
    double B;
    double C;
};

int main() {
    int n;
    cin >> n;
    cout << "INTERSECTING LINES OUTPUT" << endl;
    while (n--) {
        int x1, y1, x2, y2, x3, y3, x4, y4;
        cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
        line d1,d2;
        d1.A = y2 - y1;
        d1.B = x1 - x2;
        d1.C = d1.A*x1 + d1.B*y1;
        d2.A = y4 - y3;
        d2.B = x3 - x4;
        d2.C = d2.A*x3 + d2.B*y3;
        double d = d1.A*d2.B - d1.B*d2.A;
        if (d == 0) {
            if (d1.A*x3 + d1.B*y3 == d1.C) cout << "LINE" << endl;
            else cout << "NONE" << endl;
        } else {
            double x = 1.0*(d1.C*d2.B - d1.B*d2.C)/d;
            double y = 1.0*(d2.C*d1.A - d2.A*d1.C)/d;
            cout << setprecision(2) << fixed << "POINT " << x << " " << y << endl;
        }
    }
    cout << "END OF OUTPUT" << endl;
    return 0;
}
