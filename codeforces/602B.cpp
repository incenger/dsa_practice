#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n+1);
    int last[101000];
    for (int  i = 0 ; i < 101000; i++) last[i] = 0;
    int res = 0;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        int l1 = 0;
        if (a[i] > 2) l1 = last[a[i]-2];
        int l2 = last[a[i]+2];
        int l3 = min(last[a[i]-1], last[a[i]+1]);
        int l = max(l3, max(l1, l2));
        res = max(res, i - l);
        last[a[i]] = i;
    }
    cout << res;

    return 0;
}
