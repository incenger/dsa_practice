#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n  >> m;
    vector<vector<int> > v(n+1);
    for (int  i = 1; i <= m; i++) {
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    int index = 0;
    for (int i = 1; i <= n; i++) {
        if (v[i].size() == 0) { 
            index = i;
            break;
        }
    }
    cout << n -1 << endl;
    for (int  i = 1; i <= n; i++) {
        if (i != index) cout << i << " " << index << endl;
    }
    return 0;
}
