#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    int a[101000];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a +n);
    int res = 0;
    int j = 0;
    for (int i = 0; i < n; i++) {
        while(a[i] *2 >= a[j+1] && j < n -1) j++;
        res = max(res, j - i +1);
    }
    cout << n - res;
    return 0;
}
