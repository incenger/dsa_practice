#include <bits/stdc++.h>

using namespace std;

bool isCycle = false;
bool p = true;
vector<bool> marked(26, false);
vector<bool> onStack(26, false);
stack<int> st;
vector<string> name;
vector<vector<int> > v(26);

void dfs(int x) {
    onStack[x] = true;
    marked[x]  = true;
    for (auto next : v[x]) {
        if (!marked[next]) {
            dfs(next);
        } else if (onStack[next]) {
            isCycle = true;
        } 
    }
    onStack[x] = false;
    st.push(x);
}

int getId(char c) {
    return c - 'a';
}

void compare(string& s, string& t) {
    int length = min(s.size(), t.size());
    int si = 0, ti = 0;
    while (si < length && ti < length && s[si] == t[ti]) {
        si++;
        ti++;
    } 
    if (si >= length || ti >= length) {
        if (s > t) {
            p = false;
        } 
        return;
    }
    v[getId(s[si])].push_back(getId(t[ti]));
}

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        name.push_back(s);
    }
    for (int i = 0; i < n -1; i++) {
        compare(name[i], name[i+1]);
    }
    // for (int i = 0; i < 26; i++) {
    //     cout << i << ": ";
    //     for (auto ne : v[i]) cout << ne;
    //     cout << endl;
    // }
    
    if (!p) {
        cout << "Impossible";
        return 0;
    }
    for (int  i = 0; i < 26; i++) {
        if (!marked[i]) dfs(i);
    }
    if (isCycle) cout << "Impossible";
    else {
        while (!st.empty()) {
            cout << (char) (st.top() + 'a');
            st.pop();
        }
    }
    return 0;
}
