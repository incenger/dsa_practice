#include <bits/stdc++.h>

using namespace std;

const long long INF = 1LL << 62;

typedef pair<long long, long long> iPair;



vector<vector<iPair > >v;
priority_queue<iPair , vector<iPair >, greater<iPair> > pq;
vector<long long> dist;
vector<int> pathTo;

int main(int argc, char const *argv[])
{
    int n, m;
    cin >> n >> m;
    v = vector<vector<iPair> > (n+1);
    for (int i = 0; i < m; i++) {
        int x, y, w;
        cin >> x >> y >> w;
        v[x].push_back(make_pair(y, w));
        v[y].push_back(make_pair(x, w));
    }
    dist = vector<long long>(n+1, INF);
    pathTo = vector<int>(n+1);
    dist[n] = 0;
    pq.push(make_pair(0, n));
    while (!pq.empty()) {
        auto currentEdge = pq.top();
        pq.pop();
        auto currentVertex = currentEdge.second;

        for (auto edge : v[currentVertex]) {
            int next = edge.first;
            int weight = edge.second;

            if (dist[next] > dist[currentVertex] + weight) {
                dist[next] = dist[currentVertex] + weight;
                pathTo[next] = currentVertex;
                pq.push(make_pair(dist[next], next));
            }
        }
    }
    
    if (dist[1] == INF) cout << -1;
    else {
        int current = 1;
        while (current != n) {
            cout << current << " ";
            current = pathTo[current];
        }
        cout << n << endl;
    }
    return 0;
}
