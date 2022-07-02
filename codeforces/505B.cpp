#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int> > v[101];
bool visited[101][101] = {false};
int path;

void dfs(int a, int b, int c) {
    if(visited[b][c]) return;
    visited[b][c] = true;
    if (b == a) {
        path++;
    }
    for (int i = 0; i < v[b].size(); i++) {
        if (v[b][i].second == c) dfs(a, v[b][i].first, v[b][i].second);
    }
}




int main() {
    int n, m;
    cin >>  n >> m;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back(make_pair(b, c));
        v[b].push_back(make_pair(a, c));
    }

    int q;
    cin >> q;
    while(q--) {
        int a, b;
        cin >> a >> b;
        memset(visited, false, sizeof(visited[0][0])*100*100);
        path = 0;
        for (int i = 0; i < v[a].size(); i++) {
            dfs(a, b,v[a][i].second);
        }
        cout << path << endl;
    }
    return 0;
}
