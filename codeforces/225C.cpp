#include <iostream>
#include <bits/stdc++.h>
#define oo 10e6;

using namespace std;

char c[1001][1001];
int black[1001] = {0};
int white[1001] = {0};
int n, m, x, y;
int dp[2][1001];

int calcW(int j, int d) {
    int res = 0;
    for (int i = j -d +1; i<= j; i++ ) {
        res += white[i];
    }
    return res + dp[1][j-d];
}
    
int calcB(int j, int d) {
    int res = 0;
    for (int i = j -d +1; i<= j; i++ ) {
        res += black[i];
    }
    return res + dp[0][j-d];
}


int main() {
    cin >>  n >> m >> x >> y;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> c[i][j];
            if (c[i][j] == '#') black[j]++;
            else white[j]++;
        }
    }
    dp[0][0] = 0;
    dp[1][0] = 0;
    for (int i = 1; i <= m; i++) {
        int minB = oo;
        int minW = oo;
        for (int j = x; j <= y; j++) {
            if (i - j >= 0) {
                int w = calcW(i, j);
                int b = calcB(i, j);
                if (w < minW) minW = w;
                if (b < minB) minB = b;
            }
        }
        dp[0][i] = minW;
        dp[1][i] = minB;
    }
    cout << min(dp[1][m], dp[0][m]);
    return 0;
}
