#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int commond[100001] = {0};
    bool occur[100001] = {false};
    int prev[100001] = {-1};
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (!occur[x]) {
            occur[x] = true;
            prev[x] = i;
        } else {
            if (commond[x] == -1) continue;
            if (commond[x] == 0) {
                commond[x] = i -prev[x];
                prev[x] = i;
            } else if (commond[x] != i -prev[x]) commond[x] = -1;
            else prev[x] = i;
        }
    }
    long long res = 0;
    for (int i = 1;i <= 100000; i++){
        if (commond[i] >= 0 && occur[i]) res++;
    }

    cout << res << endl;

    for (int i = 1; i<=100000; i++) {
        if (occur[i] && commond[i] >= 0 ) cout << i << " " << commond[i] << endl;
    }
    return 0;
}
