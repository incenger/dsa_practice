#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
#define eps 1e-7

using namespace std;

int id[1000], sz[1000];

double distance(int xa, int ya, int xb, int yb) {
    double x = 1.0*(xa - xb)*(xa - xb);
    double y = 1.0*(ya - yb)*(ya - yb);
    return sqrt(x+y);
}

void init(int n) {
    for (int i = 1; i <= n; i++) {
        id[i] = i;
        sz[i] = 1;
    }
}

int findRoot(int x) {
    int root = x;
    while (root != id[root])
        root = id[root];
    while (x != root) {
        int idx = id[x];
        id[x] = root;
        x = idx;
    }
    return root;
}

bool connected(int x, int y) {
    return (findRoot(x) == findRoot(y));
}

void group(int x, int y) {
    int rootX = findRoot(x);
    int rootY = findRoot(y);
    if (rootX == rootY) return;
    if (sz[rootX] < sz[rootY]) {
        id[rootX] = rootY;
        sz[rootY] += sz[rootX];
    } else {
        id[rootY] = id[rootX];
        sz[rootX] += sz[rootY];
    }
}

struct Edge {
    int a;
    int b;
    double weight;
};

bool compare(const Edge& lhs, const Edge& rhs) {
    return lhs.weight < rhs.weight;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        init(n);
        vector<pair<int, int> > town(n+1);
        for (int i = 1; i <= n; i++) {
            int x, y;
            cin >> x >> y;
            town[i] = make_pair(x, y);
        }

        int m;
        cin >> m;
        int count = 0;
        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;
            if (!connected(a, b)) {
                group(a, b);
                count++;
            }
        }

        if (count == n-1) cout << "No new highways need" << endl;
        else {
            vector<Edge> edges;
            for (int i = 1; i <= n -1; i++) {
                for (int j = i +1; j <= n; j++) {
                    Edge e;
                    e.a = i;
                    e.b = j;
                    e.weight = distance(town[i].first, town[i].second, town[j].first, town[j].second);
                    edges.push_back(e);
                }
            }
            sort(edges.begin(), edges.end(), compare);
            for (int i = 0; i < edges.size(); i++) {
                if(!connected(edges[i].a, edges[i].b)) {
                    group(edges[i].a, edges[i].b);
                    cout << edges[i].a << " " << edges[i].b <<endl;
                }
            }
        }
        if (t != 0) cout << endl;

    }
    return 0;
}
