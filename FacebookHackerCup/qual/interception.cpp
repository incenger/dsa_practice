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
        vector<int> a(n+1);
        bool neg = false;
        for (int  i = n; i > 0; i--) {
            a[i] = p[i-1] + i;
            if (a[i] < 0) neg = false;
        }
        a[0] = 0;
        int firstZero = -1;
        for (int  i = n; i >= 0; i--) {
            if (a[i] == 0) {
                firstZero = i;
                break;
            }
        }
        firstZero ++;
        int dis = n - firstZero;
        cout << "Case #" << t << ": ";
        if (neg) {
            cout << 0;
        } else if (dis < 0) {
            cout << 0;
        } else if (dis % 2 == 0) {
            cout << 1 << endl;
            cout << fixed << setprecision(6) <<  0.0;
        } else {
            cout << 0;
        }
        if (t != T) cout << endl;
    }
    return 0;
}
