#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        int d;
        string p;
        cin >> d >> p;
        long long damage = 0;
        int current = 0;
        int numberOfShoot = 0;
        vector<int> s(p.size(), 0);
        for (int i = 0; i < p.size(); i++) {
            if (p[i] == 'C') current++;
            else { 
                damage += pow(2, current);
                s[current]++;
                numberOfShoot++;
            }
        }

        if (numberOfShoot > d) cout << "Case #" << ii << ": IMPOSSIBLE" << endl;
        else {
            int hack = 0;
            int i = p.size()-1;
            while (damage > d) {
                if(s[i] > 0) {
                    damage -= pow(2, i-1);
                    s[i]--;
                    s[i-1]++;
                    hack++;
                } else {
                    i--;
                }
            }
            cout << "Case #" << ii << ": " << hack << endl;
        }
    }
    return 0;
}
