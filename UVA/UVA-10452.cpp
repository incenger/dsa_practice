#include <iostream>

using namespace std;

int n, m, d[10];
char step[9] = "@IEHOVA#";
string a[10];

void dfs(int i, int j, int k) {
    if (i < 0 || i >= m) return;
    if (j < 0 || j >= n) return;
    if (a[i][j] == '#') {
        for (int i = 0; i < k; i++) {
            if (d[i] == 0)
                cout << "forth";
            else if (d[i] == 1)
                cout << "right";
            else if (d[i] == 2)
                cout << "left";
            if (i != k-1)
                cout << " ";
        }
        return;
    }
    if (a[i][j] != step[k])
        return;
    d[k] = 0;
    dfs(i-1, j, k+1);
    d[k] = 1;
    dfs(i, j+1, k+1);
    d[k] = 2;
    dfs(i, j-1, k+1);
    return;
}

int main()
{
    int t;
    cin >> t;
    for (int k = 0; k < t; k++) {
        cin >> m >> n;
        for (int i = 0; i < m; i++) {
            cin >> a[i];
        }
        int i = m-1;
        for (int j = 0; j < n; j++) {
            if (a[i][j] == '@') dfs(i, j, 0);
        }
        cout << endl;
    }
    return 0;
}
