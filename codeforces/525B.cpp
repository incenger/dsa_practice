#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    int n;
    cin >> n;
    vector<int> index(s.size(), 0);
    for (int  i = 0; i < n; i++) {
        int x;
        cin >> x;
        index[--x]++;
    }
    for (int i = 0; i <= (s.size()-1)/2; i++) {
        if (i > 0) index[i] += index[i-1];
        if (index[i] % 2 == 1) swap(s[i], s[s.size() -1 -i]);
    }
    cout << s;
    return 0;
}
