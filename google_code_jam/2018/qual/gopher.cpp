#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int checksurrond(bool a[][1001], int r, int c) {
    int cnt = 0;
    for (int i = r-1; i <= r+1; i++) {
        for (int j = c-1; j <= c+1; j++)
            if (!a[i][j]) cnt++;
    }
    return cnt;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a;
        cin >> a;
        int length = sqrt(a);
        int width = length;
        while (length*width < a) width++;
        bool cell[1001][1001];
        for (int i = 0; i <= 1000; i++) {
            for (int j = 0; j <= 1000; j++) {
                cell[i][j] = false;
            }
        }
        int cnt = 0;
        bool f = false;
        // phase 1
        for (int i = 2 ; i <= width -1; i++) {
            for (int j = 2; j <= length -1; j++) {
                while (checksurrond(cell, i, j)> 4) {
                    cout << i << " " << j << endl;
                    int x, y;
                    cin >> x >> y;
                    if (!cell[x][y]) {
                        cell[x][y] = true;
                        cnt++;
                    }
                }
            }
        }

        while (cnt < width*length) {
            for (int i = 2; i <= width -1; i++) {
                for (int j = 2; j <= length -1; j++) {
                    if (checksurrond(cell, i, j) > 0) {
                        cout << i << " " << j << endl;
                        int x, y;
                        cin >> x >> y;
                        if (x == 0 && y == 0) {
                            f = true;
                            break;
                        }
                        if (!cell[x][y]) {
                            cell[x][y] = true;
                            cnt++;
                        }
                    }
                }
                if (f) break;
            }
            if (f) break;
        }

    }
    return 0;
}
