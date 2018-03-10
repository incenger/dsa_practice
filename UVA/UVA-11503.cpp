#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int root[200001];
int sz[200001];

int findroot(int x) {
    int r = x;
    while (r != root[r])
        r = root[r];
    while (x != r) {
        int temp  = root[x];
        root[x] = r;
        x = temp;
    }
    return r;
}

void group(int x, int y) {
    int rootX = findroot(x);
    int rootY = findroot(y);
    if (rootX == rootY) return;
    if (sz[rootX] >= sz[rootY]) {
        root[rootY] = rootX;
        sz[rootX] += sz[rootY];
    } else {
        root[rootX] = rootY;
        sz[rootY] += sz[rootX];
    }
}

void init() {
    for (int i = 0; i < 200001; i++) {
        root[i] = i;
        sz[i] = 1;
    }
}

int size(int x) {
    return sz[findroot(x)];
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        init();
        map<string, int> index;
        int n, peopleIndex = 0;
        cin >> n;
        while(n--) {
            string s, t;
            cin >> s >> t;
            map<string, int>::iterator it;
            it = index.find(s);
            if (it == index.end()) {
                index[s] = peopleIndex;
                peopleIndex++;
            }
            it = index.find(t);
            if (it == index.end()) {
                index[t] = peopleIndex;
                peopleIndex++;
            }
            group(index[t], index[s]);
            cout << size(index[t]) << endl;
        }
    }
    return 0;
}

