#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    long long n, r, avg;
    cin >> n >> r >> avg;
    long long avgP = n * avg;
    vector<pair<long, long>> test;
    long long currentP = 0;
    for (int i = 0; i < n; i++)
    {
        long long x, y;
        cin >> x >> y;
        currentP += x;
        test.push_back(make_pair(y, x));
    }
    sort(test.begin(), test.end());
    long long res = 0;
    int i = 0;
    while (currentP < avgP)
    {
        long long add = min(avgP - currentP, r - test[i].second);
        currentP += add;
        res += test[i].first * add;
        i++;
    }
    cout << res;

    return 0;
}
