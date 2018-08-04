#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    vector<bool> v(n + 1, false);
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        if (x <= n)
            v[x] = true;
    }
    int res = 0;
    for (int i = 1; i < v.size(); i++)
    {
        res += (v[i]) ? 0 : 1;
    }
    cout << res;
    return 0;
}
