#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n;
    cin >> n;
    vector<long long> s(n);
    for (int i = 0; i < n; i++) {
        cin >> s[i];
        if (i > 0) s[i] += s[i-1]; 
    }
    long long sum = s[n-1];
    long long res  = 0;
    vector<int> c(n, 0);
    vector<int> sc(n+2, 0);
    for (int i = n-2; i >= 0; i--) {
        if (sum - s[i] == sum/3) c[i+1]++;
        sc[i+1] = sc[i+2] + c[i+1];
    }

    if (sum % 3 == 0) {
        for (int i = 0; i < n; i++) {
            if (s[i] == sum/3) {
                res += sc[i+2];
            }
        } 
    }
    cout << res;
    return 0;
}
