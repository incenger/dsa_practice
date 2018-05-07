#include <iostream>
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t<= T; t++) {
        int n, l;
        cin >> n >> l;
        vector<int> fixed(l);
        int cnt = 0;
        for (int i= 0; i < l; i++) { 
            cin >> fixed[i];
            cnt += fixed[i];
        }
        bool f = true;
        int remain = n-cnt;
        double x = 100.0/n;
        if (round(x) < x) { 
            f = false;
        }
        int res = 0;
        if (f) {
            for (auto s : fixed) {
                res += static_cast<int> (round(100.0*s/n));
            }
            res += static_cast<int> (round(x))*remain;
        } else {
            if (remain > 1) {
                x*= 2;
                res += static_cast<int> (round(x)*(remain/2));
                int left = res % 2;
                if (left == 1) {
                    for (auto& s : fixed) {
                        if (round(100.0*(s+1)/n) > 100.0*s/n) {
                            s++;
                            left--;
                            break;
                        }
                    }
                    for (auto s : fixed) {
                        res += static_cast<int> (round(100.0*s/n));
                    }
                    res += static_cast<int> (round(100.0*left/n));
                }

            } else {
                int left = 1;
                for (auto& s : fixed) {
                    if (round(100.0*(s+1)/n) > 100.0*s/n) {
                        s++;
                        left--;
                        break;
                    }
                }
                for (auto s : fixed) {
                    res += static_cast<int> (round(100.0*s/n));
                }
                res += static_cast<int> (round(100.0*left/n));
            } 
        }
        cout << "Case #"<< t << ": " << res << endl;
    }
    return 0;
}
