#include <bits/stdc++.h>

using namespace std;

vector<vector<int> > v;
vector<bool> checked;
vector<bool> color;
bool b2 = true;

void dfs(int s, int t) {
    checked[s] = true;
    for (auto next : v[s]) {
        if (!checked[next]) {
            color[next] = !color[s];
            dfs(next, s);
        } else if (color[next] == color[s]) {
            b2 = false;
        }
    }
}

int main(int argc, char const *argv[])
{
    int n,m;
    cin >> n >> m;
    v = vector<vector<int> >(n+1, vector<int>());
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    checked = vector<bool>(n+1, false);
    color = vector<bool>(n+1, false);
    for (int  i = 1; i <= n; i++) {
        if (!checked[i]) {
            dfs(i, 0);
        }
    }
    // for (auto c : color) cout << c << " ";
    if (b2) {
        int a = 0, b= 0;
        for (int i = 1; i <= n; i++) {
            if (color[i]) a++;
            else b++;
        }
        cout << a << endl;
        for (int i = 1; i <= n; i++) {
            if (color[i]) cout << i << " ";
        }
        cout << endl;
        cout << b << endl;
        for (int i = 1; i <= n; i++) {
            if (!color[i]) cout << i << " ";
        }
    } else {
        cout << -1;
    }
    return 0;
}