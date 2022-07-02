#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> p;
vector<int> v;
vector<bool> marked;
vector<int> value;
vector<int> pos;

void dfs(int x)
{
    marked[x] = true;
    pos.push_back(x);
    value.push_back(v[x]);
    for (auto &next : p[x])
    {
        if (!marked[next])
            dfs(next);
    }
}

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    p = vector<vector<int>>(n);
    marked = vector<bool>(n, false);
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            char x;
            cin >> x;
            if (x == '1')
            {
                p[i].push_back(j);
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (!marked[i])
        {
            pos.clear();
            value.clear();
            dfs(i);
        }
        sort(pos.begin(), pos.end());
        sort(value.begin(), value.end());
        for (int j = 0; j < pos.size(); j++)
        {
            v[pos[j]] = value[j];
        }
    }
    for (auto i : v)
        cout << i << " ";
    return 0;
}
