#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        vector<int> odd;
        vector<int> even;
        int n;
        cin >> n;
        for (int ii = 0; ii < n; ii++) {
            int x;
            cin >> x;
            if (ii % 2 == 0) even.push_back(x);
            else odd.push_back(x);
        }
        sort(even.begin(), even.end());
        sort(odd.begin(), odd.end());
        vector<int> origin;
        for (int ii = 0; ii < even.size(); ii++) {
            origin.push_back(even[ii]);
            if (ii < odd.size()) origin.push_back(odd[ii]);
        }
        int f = -1;
        for (int ii = 0; ii < origin.size() -1; ii++) {
            if (origin[ii] > origin[ii+1]) {
                f = ii;
                break;
            }
        }
        if (f >= 0) cout << "Case #" << i << ": " << f << endl;
        else cout << "Case #" << i << ": " << "OK" << endl;
    }
    return 0;
}
