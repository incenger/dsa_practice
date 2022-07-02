#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    if (n > 26) {
        cout << -1;
    } else {
        vector<int> ch(26, 0);
        for (int  i = 0; i < s.size(); i++) {
            ch[s[i]-'a']++;
        }
        int res = 0;
        for (auto i : ch) {
            res += (i == 0) ? 0 : (i-1);
        }
        cout << res;
    }
    return 0;
}
