#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[]) {
    int n;
    cin >> n;
    vector<long long> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    long long m = *max_element(v.begin(), v.end());
    long long s = accumulate(v.begin(), v.end(), 0LL);
    cout << max(m, s/(n-1) + !(s %(n-1) == 0));
    
    return 0;
}
