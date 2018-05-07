#include <iostream>
#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

class SortEstimate {
    private:
        double eps = 1e-10;
    public:
        double howMany(int c, int t) {
            double lo = 0.0;
            double hi = 8e7;
            double mid = 0.0;
            while (abs(lo - hi) > eps) {
                mid = lo + (hi-lo)/2;
                double res = c*mid*log2(mid);
                cout << mid << " " << res << endl;
                if (res < t) lo = mid;
                else if (res > t) hi = mid;
                else return mid;
            }
            return mid;
        }
    
};


int main(int argc, char const* argv[]) {
    SortEstimate se;
    int c, t;
    cin >> c >> t;
    cout << fixed << setprecision(9) << se.howMany(c, t) << endl;
    return 0;
}
