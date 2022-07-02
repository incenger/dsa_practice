#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    vector<int> c(26, 0);
    int odd = 0;
    for (auto ch : s) c[ch-'a']++;
    for (auto x : c) {
        if (x % 2 == 1) odd++;
    }
    if (odd  == 0 || odd % 2 == 1 ) cout << "First";
    else cout << "Second";
    return 0;
}
