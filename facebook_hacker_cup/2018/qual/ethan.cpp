#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    freopen("INPUT.TXT", "rt", stdin);
    freopen("OUTPUT.TXT", "wr", stdout);
    int T;
    cin >> T;
    for (int  t = 1;  t <= T; t++) {
        string s;
        cin >> s;
        char firstC = s[0];
        int next = -1;
        for (int  i = 1; i < s.size(); i++) {
            if (s[i] == firstC) {
                next = i;
                break;
            }
        }
        cout << "Case #" << t << ": ";
        if (next == -1) {
            cout << "Impossible";
        } else {
            string prefix = s.substr(0, next);
            string res = prefix + s;
            if (res.find(s) == 0) {
                cout <<  "Impossible";
            } else {
                cout <<  res;
            }
        }
        if (t != T) cout << endl;
    }
    return 0;
}
