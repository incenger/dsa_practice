#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool isSubsequence(const string& a, const  string& b, int aIndex, int bIndex) {
    if (aIndex == a.size()) return true;
    else if (bIndex == b.size()) return false;
    else if (a[aIndex] == b[bIndex]) return isSubsequence(a, b, aIndex+1, bIndex+1);
    else return isSubsequence(a, b, aIndex, bIndex+1);
}


int main(int argc, char const* argv[]) {
    string t, p;
    cin >> t >> p;
    vector<int> v(t.size());
    for (int i = 0; i < v.size(); i++) {
        cin >> v[i];
    }
    int lo = 0;
    int hi = v.size();
    string s;
    string res;
    while (lo < hi) {
        int mi = (lo +hi+1)/2;
        s = t;
        for (int  i = 0 ; i < mi; i++) {
            s[v[i]-1] = '_';
        }
        res = "";
        for (int  i = 0; i < s.size(); i++) {
            if (s[i] != '_') res+= s[i];
        }
        // cout << lo << " " << hi << " " << mi << " " << res << endl;
        if (isSubsequence(p, res, 0, 0)) {
            lo = mi;
        } else hi = mi-1;
    }
    cout << lo; 
    return 0;
}
