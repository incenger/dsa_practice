#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int id[101], sz[101];

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
    int v;
    int w;
    int weight;
    int index;
    bool used;
};

struct EdgeCompare {
    bool operator() (const Edge& lhs, const Edge& rhs) const {
        return lhs.weight > rhs.weight;
    }
};

int main() {
    int t;
    cin >> t;
    while(t--) {
        int v, e;
        cin >> v >> e;
        vector<Edge> edges;
        priority_queue<Edge, vector<Edge>, EdgeCompare> pq;
        for (int i = 0; i < e; i++) {
            Edge edge;
            int a, b, c;
            cin >> a >> b >> c;
            edge.v = a;
            edge.w = b;
            edge.weight = c;
            edge.used = true;
            edge.index = i;
            edges.push_back(edge); 
            pq.push(edge);
        }
        int count = 0;
        int cost = 0;
        vector<int> mst;
        init(v);
        while (!pq.empty() && count < v -1) {
            Edge edge = pq.top();
            pq.pop();
            if(!connected(edge.w, edge.v) && edge.used) {
                group(edge.w, edge.v);
                count++;
                cost += edge.weight;
                mst.push_back(edge.index);
            }
        }
        cout << cost << " ";
        int cost2 = 987654321;
        for (int i = 0; i < mst.size(); i++) {
            edges[mst[i]].used = false;

            priority_queue<Edge, vector<Edge>, EdgeCompare> pq2;

            for (int j = 0; j < e; j++) {
                pq2.push(edges[j]);
            }
            count = 0;
            cost = 0;
            init(v);
            while (!pq2.empty()) {
                Edge edge = pq2.top();
                pq2.pop();
                if (!edge.used) continue;
                if(!connected(edge.w, edge.v)) {
                    group(edge.w, edge.v);
                    count++;
                    cost += edge.weight;
                }
            }
            if (count == v -1) 
                if (cost < cost2) cost2 = cost;
            edges[mst[i]].used = true;
        }
        cout << cost2 << endl;
    }
    return 0;
}
