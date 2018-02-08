#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    char c[100][100];
    memset(c, 'S', sizeof(c));
    int maxIsland = (n*n +1)/2;
    if (k > maxIsland) cout << "NO";
    else {
        int island = 0;
        for (int i = 0; i < n; i++) {
            if (island >= k) break;
            for (int j = i%2; j < n; j+= 2) {
                if (island >= k) break;
                c[i][j] = 'L';
                island++;
            }
        }
        cout << "YES" << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << c[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
