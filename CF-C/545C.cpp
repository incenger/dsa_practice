#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    pair<int, int> p[100001];
    cin >> n;
    for (int i =1 ; i <= n; i++) {
        int x, y;
        cin >> x >> y;
        p[i] = make_pair(x, y);
    }
    int fell = 0;
    for (int i = 1; i <= n; i++) {
        if (i == 1) fell++;
        else if (i == n) fell++;
        else {
            if (p[i].first - p[i].second > p[i-1].first) {
                fell++;
            }
            else if (p[i].first + p[i].second < p[i+1].first) {
                fell++;
                p[i].first = p[i].first + p[i].second;
            }
        }
    }
    cout << fell;
    return 0;
}
