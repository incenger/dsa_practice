#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool isBeautiful(string s) {
    if (s.size() == 1) {
        return (s == "1" || s== "0");
    }
    for (int i  = 0; i < s.size(); i++) {
        if (s[0] != '1') return false;
        if (i!= 0 && s[i] != '0') return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    vector<string> a(n);
    bool zero = false;
    bool beau = true;
    string res;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] == "0") zero =true;
        if (isBeautiful(a[i])) res += a[i].substr(1);
        else { 
            res = a[i] + res;
            beau = false;
        }
    }
    if (!zero && beau) res = "1" +res;
    if (zero) cout << 0;
    else cout << res;
    return 0;
}
