#include <bits/stdc++.h>

using namespace std;

char v[501][501];
int n;
int m;
bool f = true;

bool valid(int i, int j)
{
    return (0 <= i && i < n && 0 <= j && j < m);
}

void check(int i, int j)
{
    if (valid(i + 1, j) && v[i + 1][j] == 'W')
        f = false;
    if (valid(i - 1, j) && v[i - 1][j] == 'W')
        f = false;
    if (valid(i, j + 1) && v[i][j + 1] == 'W')
        f = false;
    if (valid(i, j - 1) && v[i][j - 1] == 'W')
        f = false;
}

int main(int argc, char const *argv[])
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> v[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (v[i][j] == 'S')
                check(i, j);
            else if (v[i][j] == '.')
                v[i][j] = 'D';
        }
    }
    if (!f)
        cout << "No";
    else
    {
        cout << "Yes" << endl;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cout << v[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
