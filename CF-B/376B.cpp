#include <iostream>
#include <bits/stdc++.h>


using namespace std;

int main() {
    int man[101] = {0};
    int n, m;
    cin >> n >> m;
    while(m--) {
        int a, b, c;
        cin >> a >> b >> c;
        man[a] -= c;
        man[b] += c;
    }
    long long res = 0;
    for (int i = 1; i <= n; i++) {
        if (man[i]  < 0) res += man[i];
    }
    cout << -res;
    return 0;
}

