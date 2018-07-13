#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{

    freopen("INPUT.TXT", "rt", stdin);
    freopen("OUTPUT.TXT", "wr", stdout);
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; t++)
    {
        int n;
        cin >> n;
        vector<int> p(n+1);
        for (int i = n; i >= 0; i--) {
            cin >> p[i];
        }
        cout << "Case #" << t << ": ";
        if (n % 2 == 1) {
            cout << 1 << endl;
            cout << fixed << setprecision(6) <<  0.0;
        } else {
            cout << 0;
        }
        if (t != T) cout << endl;
    }
    return 0;
}
