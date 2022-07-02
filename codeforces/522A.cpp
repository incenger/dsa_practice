#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    map<string, int> mp;
    vector<vector<int> > v(n+1, vector<int>());
    vector<int> distTo(n+1, 1);
    vector<bool> checked(n+1, false);
    queue<int> q;
    mp["polycraph"] = 0;
    for (int i = 0; i < n; i++) {
        string name1, get, name2;
        cin >> name1 >> get >> name2;
        transform(name1.begin(), name1.end(), name1.begin(), ::tolower);
        transform(name2.begin(), name2.end(), name2.begin(), ::tolower);
        mp[name1] = i+1; 
        // cout << mp[name1] << " " << mp[name2] << endl;
        v[mp[name1]].push_back(mp[name2]);
        v[mp[name2]].push_back(mp[name1]);
    }
    q.push(0);
    while (!q.empty()) {
        int vertex = q.front();
        checked[vertex] = true;
        q.pop();
        for (auto next : v[vertex]) {
            if (!checked[next]) {
                distTo[next] = distTo[vertex] +1;
                q.push(next);
            }
        }
    }
    int res = 0;
    for (auto l : distTo) {
        if (l > res) res = l;
    }
    cout << res;
    return 0;
}
