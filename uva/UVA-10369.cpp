#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int id[1000], sz[1000];

double distance(int xa, int ya, int xb, int yb) {
    double x = 1.0*(xa - xb)*(xa - xb);
    double y = 1.0*(ya - yb)*(ya - yb);
    return sqrt(x+y);
}

void init(int n) {
    for (int i = 0; i < n; i++) {
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

struct Point {
    int x;
    int y;
};

int main() {

    int n;
    cin >> n;
    while (n--) {
        int s, p;
        cin >> s >> p;
        init(p);
        vector<int> x(p);
        vector<int> y(p);
        for (int i = 0; i < p; i++)
            cin >> x[i] >> y[i];
        vector<Edge> edges;
        for (int i = 0; i < p-1; i++) {
            for (int j = i+1; j < p; j++) {
                Edge e;
                e.a = i;
                e.b = j;
                e.weight = distance(x[i], y[i], x[j], y[j]);
                edges.push_back(e);
            }
        }
        sort(edges.begin(), edges.end(), compare);
        int i = 0;
        int edgesnum = 0;
        double result = 0;
        while (edgesnum < p - s) {
            Edge e = edges[i++];
            int a = e.a;
            int b = e.b;
            if(!connected(a,b)) {
                result = max(result, e.weight);
                edgesnum++;
                group(a, b);
            }
        }
        // for (int i = 0; i < res.size(); i++)
        //     cout << res[i] << " ";
        cout << fixed << setprecision(2) << result << endl;
    }
    return 0;
}
