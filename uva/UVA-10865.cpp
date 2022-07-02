#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    pair<int,int> p[200000];
    while (true) {
        cin >> n;
        if (n == 0) break;
        for (int i = 0; i < n; i++) {
            cin >> p[i].first >> p[i].second;
        }
        int lineX = p[n/2].first;
        int lineY = p[n/2].second;
        int stan = 0, ollie = 0;
        for (int i = 0; i < n; i++) {
            int x = p[i].first;
            int y = p[i].second;
            if ((x > lineX && y > lineY) || (x < lineX && y < lineY)) stan++;
            if ((x >lineX && y < lineY) || (x<lineX && y > lineY)) ollie++;
        }
        cout << stan << " " << ollie << endl;
    }
    return 0;
}

