#include <bits/stdc++.h>

using namespace std;
vector<vector<char> > c; 
int n;
const long long MOD = 1000000007;

long long count(int i) {
    long long res = 2;
    if (c[0][i] == '#' || c[0][i+1] == '#') res--;
    if (c[2][i] == '#' || c[2][i+1] == '#') res--;
    if (c[1][i] == '#' || c[1][i+1] == '#') res = 0;
    return res;
}



int main(int argc, char const *argv[])
{
    freopen("let_it_flow.txt", "rt", stdin);
    freopen("OUTPUT.TXT", "wr", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> n;
        c = vector<vector<char> > (3, vector<char>(n));
        for (int  i = 0; i < 3; i++) {
            for (int j = 0; j < n; j++) {
                cin >> c[i][j];
            }
        }
        long long res = 1;
        if (c[0][0] == '#' || c[1][0] == '#' || c[1][n-1] == '#' || c[2][n-1] == '#') res = 0;
        if (n % 2 == 1) res = 0;
        else  {
            for (int i  = 1; i < n -1; i +=2) {
                res = (res*count(i)) % MOD;
            }
        }
        cout << "Case #" << t <<": " << res;
        if (t != T) cout << endl;
    }
    return 0;
}
