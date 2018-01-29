#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    pair<pair<int, int>, int> a[1000];
    int xa, ya, xb, yb;
    cin >> xa >> ya >> xb >> yb;
    if (xa > xb) swap(xa, xb);
    if (ya > yb) swap(ya, yb);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x, y, r;
        cin >> x >> y >> r;
        a[i].first = make_pair(x, y);
        a[i].second = r;
    }

    int res = 0;
    for (int i = xa; i <= xb; i++) {
        for (int j = ya; j <= yb; j++) {
            if (i != xa && i != xb && j!= ya && j!= yb) continue;
            bool heat = false;
            for (int k = 0; k < n; k++) {
                if (heat) break;
                int x = a[k].first.first;
                int y = a[k].first.second;
                double dis = pow((i -x),2) + pow((j-y), 2);
                if (dis <= a[k].second*a[k].second) heat = true;
            }
            if (!heat) res++;
        }
    }
    cout << res;
    return 0;
}
