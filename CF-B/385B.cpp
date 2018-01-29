#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    int j = 0;
    long long res = 0;
    int l = s.length();
    for (int i = 0; i < l -3; i++) {
        if (s[i] == 'b' && s[i+1] == 'e' && s[i+2] == 'a' && s[i+3] == 'r') {
            res += (i - j +1)*(l - (i+3));
            j = i+1;
        }
    }
    cout << res;
    return 0;
}
