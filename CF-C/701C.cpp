#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<vector<int> > a(200, vector<int>(100005, 0));
    for (int  i = 0; i < n; i++) {
        for (char c = 'A'; c <= 'Z'; c++) {
            a[(int)c][i+1] = a[(int)c][i] + (s[i]==c);
        }
        for (char c = 'a'; c <= 'z'; c++) {
            a[(int)c][i+1] = a[(int)c][i] + (s[i]==c);
        }
    }
    set<char> type;
    for (int i = 0; i < s.size(); i++) {
        type.insert(s[i]);
    }
    int types = type.size();
    int res = n;
    for (int i = 0; i < n; i++) {
        int lo = types;
        int hi = res;
        bool d = false;;
        while (lo < hi) {
            int mi = (lo + hi)/2;
            bool f = true;
            for (auto& c : type) {
                if (a[(int)c][i+mi]-a[(int)c][i] < 1) {
                    f = false;
                    break;
                }
            }
            if (f) {
                hi = mi;
                d = true;
            } else {
                lo = mi +1;
            }
        }
        if (d) res = min(res, lo);
    }
    cout << res;
    return 0;
}
