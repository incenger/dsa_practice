#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int main() {
    string a, b;
    cin >> a >> b;
    vector<vector<int>> d(b.size()+1, vector<int>(2, 0));
    for (int i = 1; i <= b.size(); i++) {
        d[i][0] = d[i-1][0];
        d[i][1] = d[i-1][1];
        if (b[i-1] == '1') d[i][1]++;
        if (b[i-1] == '0') d[i][0]++;
    }
    long long res = 0;
    for (int  i = 0 ; i < a.size(); i++) {
        for (int j = 0; j < 2; j++) {
            res += abs(a[i] -'0'- j)*abs(d[b.size() - a.size() + i +1][j] - d[i][j]);
        }
    }
    cout << res;
    return 0;
}
