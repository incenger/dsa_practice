#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n >> m;
    vector<int> v(n+1);
    for (int  i = 1; i <= n; i++) {
        cin >> v[i];
    }
    int total = 0;
    for (int  i  = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        total += min(v[x], v[y]);
    }
    cout << total;
    return 0;
}
