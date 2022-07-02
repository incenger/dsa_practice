#include <bits/stdc++.h>

using namespace std;
int n, k;

struct Node {
    int l;
    int r;
};

vector<Node> nodes;
vector<int> preRes;
vector<int> postRes;
vector<set<int> >g;
vector<bool> checked;
vector<int> res;
int cnt;

void dfs(int x) {
    res[x] = cnt;
    checked[x] = true;
    for(auto next : g[x]) {
        if (!checked[next]) dfs(next);
    }
}

void pre(int i) {
    if (i == 0) return;
    preRes.push_back(i);
    pre(nodes[i].l);
    pre(nodes[i].r);
}

void post(int i) {
    if (i == 0) return;
    post(nodes[i].l);
    post(nodes[i].r);
    postRes.push_back(i);
}

int main(int argc, char const *argv[])
{
    freopen("INPUT.TXT", "rt", stdin);
    freopen("OUTPUT.TXT", "wr", stdout);
    int T;
    cin >> T;
    for (int  t = 1; t <= T; t++) {
        cin >> n >> k;
        nodes =  vector<Node>(n+1);
        g =  vector<set<int> > (n+1, set<int>());
        checked =  vector<bool> (n+1, false);
        res = vector<int>(n+1);
        preRes = vector<int>();
        postRes = vector<int>();
        
        for (int i = 1; i <= n; i++) {
            Node node;
            cin >> node.l >> node.r;
            nodes[i] =  node;
        }
        pre(1); post(1);
        for (int  i = 0; i < n; i++) {
            if (preRes[i] != postRes[i]) {
                g[preRes[i]].insert(postRes[i]);
                g[postRes[i]].insert(preRes[i]);
            }
        }

        bool f = false;

        cnt = 1;

        for (int  i = 1; i <= n; i++) {
            if (!checked[i]) {
                dfs(i);
                cnt++;
                if (cnt > k) {
                    cnt =  1;
                    f= true;
                }
            }
        }
        cout <<  "Case #" << t <<": ";
        if (!f) cout << "Impossible";
        else {
            for (int  i = 1; i <= n; i++) cout << res[i] << " ";
        }
        if (t != T) cout << endl;
    }
    return 0;
}
