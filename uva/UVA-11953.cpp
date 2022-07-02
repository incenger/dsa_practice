#include <iostream>
#include<bits/stdc++.h>


using namespace std;

char a[100][100];
bool vis[100][100];
int n;

int dfs(int i, int j) {
    if (i < 0 || i >= n) return 0;
    if (j < 0 || j >= n) return 0;
    if (a[i][j] == '.') return 0;
    if (a[i][j] == '@') return 0;
    if (vis[i][j]) return 0;
    vis[i][j] = true;
    return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1);
}

int main()
{
    int test;
    cin >> test;
    while(test--) {
        cin >> n;
        memset(vis, false, sizeof vis);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> a[i][j];
            }
        }
        int ship = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] == 'x' && !vis[i][j])
                    if (dfs(i, j) > 0) ship++;
            }
        }
        cout << ship << endl;
    }
    return 0;
}
