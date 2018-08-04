#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    vector<pair<pair<int, int>, int>> req(n);
    for (int i = 0; i < n; i++)
    {
        int c, p;
        cin >> c >> p;
        req[i] = make_pair(make_pair(p, c), i + 1);
    }
    int m;
    cin >> m;
    vector<pair<int, int>> table(m);
    for (int i = 0; i < m; i++)
    {
        int cap;
        cin >> cap;
        table[i] = make_pair(cap, i + 1);
    }
    vector<bool> mark(m + 1, false);
    sort(req.begin(), req.end());
    reverse(req.begin(), req.end());
    sort(table.begin(), table.end());
    int total = 0;
    vector<pair<int, int>> res;
    for (auto &re : req)
    {
        for (auto &tb : table)
        {
            if (tb.first >= re.first.second && !mark[tb.second])
            {
                total += re.first.first;
                res.push_back(make_pair(re.second, tb.second));
                mark[tb.second] = true;
                break;
            }
        }
    }
    cout << res.size() << " " << total << endl;
    for (auto &p : res)
    {
        cout << p.first << " " << p.second << endl;
    }
    return 0;
}
