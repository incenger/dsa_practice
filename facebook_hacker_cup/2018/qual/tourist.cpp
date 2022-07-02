#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const* argv[])
{
    freopen("INPUT.TXT", "rt", stdin);
    freopen("OUTPUT.TXT", "wr", stdout);
    int T;
    cin >> T;
    for (int  t = 1; t <= T; t++) {
        int n, k;
        cin >> n >> k;
        long long v;
        cin >> v;
        vector<string> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        int pos = ((v-1)%n) * k;
        pos %= n;
        vector<int> see;
        for (int i = 0; i < k; i++) {
            see.push_back(pos);
            pos = (pos+1) % n;
        }
        sort(see.begin(), see.end());
        cout << "Case #" << t << ": ";
        for (auto& x : see) {
            // cout << x << " ";
            cout << a[x] << " ";
        }
        if (t != T) cout << endl;
    }
    return 0;
}
