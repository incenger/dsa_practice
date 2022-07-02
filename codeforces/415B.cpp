#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, a, b;
    cin >> n >> a >>b;
    vector<long long> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        long long x = v[i]*a/b;
        long long y = x*b/a + ((x*b) % a > 0); 
        cout << v[i] - y << " ";
    }
    return 0;
}
