#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n >> m;
    bool v[505][505];
    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        x--;
        y--;
        v[x][y] = true;
        v[y][x] = true;
    }
    int res;
    if (!v[0][n - 1])
    {
        vector<int> dist(n, -1);
        dist[0] = 0;
        queue<int> q;
        q.push(0);
        vector<bool> mark(n, false);
        while (!q.empty() && !mark[n - 1])
        {
            int current = q.front();
            q.pop();
            for (int i = 0; i < n; i++)
            {
                if (v[current][i] && !mark[i])
                {
                    q.push(i);
                    mark[i] = true;
                    if (dist[i] == -1)
                        dist[i] = dist[current] + 1;
                }
            }
        }
        if (dist[n - 1] == -1)
            res = -1;
        else
            res = max(1, dist[n - 1]);
    }
    else
    {
        vector<int> dist(n, -1);
        dist[0] = 0;
        queue<int> q;
        q.push(0);
        vector<bool> mark(n, false);
        while (!q.empty() && !mark[n - 1])
        {
            int current = q.front();
            q.pop();
            for (int i = 0; i < n; i++)
            {
                if (!v[current][i] && !mark[i])
                {
                    q.push(i);
                    mark[i] = true;
                    if (dist[i] == -1)
                        dist[i] = dist[current] + 1;
                }
            }
        }
        if (dist[n - 1] == -1)
            res = -1;
        else
            res = max(1, dist[n - 1]);
    }
    cout << res;
    return 0;
}
