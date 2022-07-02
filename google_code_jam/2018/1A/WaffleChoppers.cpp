#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int countChoco(vector<vector<char>>& cell, int bc, int ec, int br, int er) {
    int res = 0;
    for (int  i = br; i <= er; i++) {
        for (int j = bc; j <= ec; j++) {
            if (cell[i][j] == '@') res++;
        }
    }
    return res;
}

vector<int> isDividedVertical(vector<vector<char>>& cell, int n, int m, int b, int e, int v) {
    vector<int> res;
    vector<int> c(m, 0);
    for (int  i = b;i <= e; i++) {
        for (int j = 0; j < n; j++) {
            if (cell[j][i] == '@') c[i]++;
        }
    }
    int sum  = accumulate(c.begin(), c.end(), 0);
    if (sum % (v+1) != 0) return res;
    int part  = sum/(v+1);
    int i = b;
    int sumpart  = 0;
    while (i <= e) {
        while (sumpart < part) sumpart += c[i++];
        if (sumpart == part) {
            sumpart = 0;
            res.push_back(i-1);
        } else break;
    }
    return res;
}

vector<int> isDividedHorizontal(vector<vector<char>>& cell, int n, int m, int b, int e, int h) {
    vector<int> res;
    vector<int> r(n, 0);
    for (int  i = 0;i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (cell[i][j] == '@') r[i]++;
        }
    }
    int sum  = accumulate(r.begin(), r.end(), 0);
    if (sum % (h+1) != 0) return res;
    int part  = sum/(h+1);
    int i = 0;
    int sumpart  = 0;
    while (i < n) {
        while (sumpart < part) sumpart += r[i++];
        if (sumpart == part) {
            sumpart = 0;
            res.push_back(i-1);
        } else break;
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, m, h, v;
        cin >> n >> m >> h >> v;
        int cnt = 0;
        vector<vector<char>> cell(n, vector<char>(m));
        for (int  i = 0; i < n; i++) {
            for (int  j = 0; j < m; j++) {
                cin >> cell[i][j];
                if (cell[i][j] == '@')cnt++;
            }
        }
        bool able =true;
        if ((cnt)%((h+1)*(v+1)) != 0) able = false;
        if (cnt == 0){
            cout << "Case #" << t <<": POSSIBLE" << endl; 
            continue;
        }         
        vector<int> c = isDividedVertical(cell, n, m, 0, m-1, v);
        vector<int> r = isDividedHorizontal(cell, n, m, 0, n-1, h);
        if (c.size() != v +1) able = false;
        if (r.size() != h+1) able = false;
        if (able) {
            int prevC = 0;
            for (int  i = 0; i < c.size(); i++) {
                int prevR = 0;
                for (int j = 0; j < r.size(); j++) {
                    int cntchoco = countChoco(cell, prevC, c[i], prevR, r[j]);
                    if (cntchoco != (cnt/((h+1)*(v+1)))) {
                        able = false;
                    }
                    prevR = r[j]+1;

                }
                prevC = c[i]+1;
            }
        }
        cout << "Case #" << t <<": ";
        if (able) cout << "POSSIBLE" << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
