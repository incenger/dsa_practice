#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    int res = 0;
    vector<int> v(n);
    for (int  i = 0; i < n; i++) {
        cin >> v[i];
    }
    for (int  i = 0; i < n; i++) {
        if (v[i] == 1) {
            if (i == 0) res++;
            else if (v[i-1] == 1) res++;
            else if (res == 0) res ++;
            else res += 2;
        } 
    }
    cout << res;
    return 0;
}
