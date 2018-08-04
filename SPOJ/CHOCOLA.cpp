#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        int m, n;
        cin >> m >> n;
        vector<pair<int, int>> cost;
        for (int i = 0; i < m - 1; i++)
        {
            int x;
            cin >> x;
            cost.push_back(make_pair(x, 0));
        }
        for (int i = 0; i < n - 1; i++)
        {
            int x;
            cin >> x;
            cost.push_back(make_pair(x, 1));
        }
        sort(cost.begin(), cost.end());
        reverse(cost.begin(), cost.end());
        int ver = 0;
        int hor = 0;
        long long res = 0;
        for (auto &p : cost)
        {
            if (p.second == 0)
            {
                res += p.first * (hor + 1);
                ver++;
            }
            else
            {
                res += p.first * (ver + 1);
                hor++;
            }
        }
        cout << res << endl;
    }
    return 0;
}
