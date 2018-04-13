#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int a[101][101];
int b[101][101];
int d[101][101];
int m, n;

void printA() {
    for (int  i =1 ; i <= m; i++) {
        for (int j  =1; j <= n; j++)
            cout << a[i][j] << " ";
        cout << endl;
    }
}

bool check() {
    for (int i = 1; i <= m; i++) {
        for (int j  =1;  j <= n; j++) {
            if (a[i][j]) {
                for (int  r = 1; r <= m; r++)
                    d[r][j] = 1;
                for (int  c = 1; c <= n; c++)
                    d[i][c] = 1;
            }
        }
    }
    for (int  i =1;i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (d[i][j]!= b[i][j]) return false;
    return true;
}

void make0(int r, int c) {
    for (int i = 1; i <= n; i++)
        a[r][i] = 0;
    for (int i = 1; i <= m; i++)
        a[i][c] = 0;
}

int main() {
    cin >> m >> n;
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            cin >> b[i][j];
            a[i][j] = 1;
        }

    for (int  i = 1; i <= m; i++) {
        for (int j = 1; j<= n; j++) {
            if (!b[i][j]) make0(i, j);
        }
    }
    if (check()) {
        cout << "YES" << endl;
        printA();
    } else cout << "NO";
    return 0;
}
