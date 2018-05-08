#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    map<string , bool> M;
    int n, m;
    cin >> n >> m;
    int a = 0;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        M[s] = true;
    }
    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;
        if (M[s]) a++;
    }

    if (a % 2 == 1) {
        if (n>= m) cout << "YES";
        else cout << "NO";
    } else {
        if (n > m) cout << "YES";
        else cout << "NO";
    }
    return 0;
}
