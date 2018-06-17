#include <iostream>
#include <bits/stdc++.h>
#include <bits/stdc++.h>


using namespace std;

int main(int argc, char const* argv[]) {
    int k;
    cin >> k;
    string s;
    cin >> s;
    long long res= 0;
    vector<int> a(s.size()+1, 0);
    for (int i = 0; i < s.size(); i++) {
        a[i+1] = a[i] + (s[i] == '1');
    }
    vector<int> b(s.size()+1, 0);
    for (int i = 0; i < a.size(); i++) {
        b[a[i]]++;
    }
    if (k == 0) {
        for (int i = 0; i < b.size(); i++) {
            res += (long long)(b[i]) *(b[i] -1)/2;
        }
    } else {
        for (int i = 0; i < b.size(); i++) {
            if (i - k >= 0) res += (long long)(b[i]) * b[i-k];

       }
    }
    cout << res;
    return 0;
}
