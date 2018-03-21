#include <bits/stdc++.h>

using namespace std;

long long stoneDivision(long long n, vector<long long> &s, unordered_map<long long, long long> &dp) {
    // Complete this function
    if (n == 0 || n == 1) return 0;
    
    if (dp.find(n) != dp.end()) return dp[n];
    
    long long maxMove = 0;
    
    for (int i = 0; i < s.size(); i++) {
        long long move = 0;
        if (n % s[i] != 0 || n == s[i]) continue;
        long long piles  = n/s[i];
        move += stoneDivision(s[i], s, dp)*piles;
        move++;
        if (move > maxMove) maxMove = move;
    }
    dp.insert(make_pair(n, maxMove));
    return maxMove;
}

int main() {
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        long long n;
        int m;
        cin >> n >> m;
        vector<long long> s(m);
        for(int s_i = 0; s_i < m; s_i++){
           cin >> s[s_i];
        }
        unordered_map<long long, long long> dp; 
        long result = stoneDivision(n, s, dp);
        cout << result << endl;
    }
    return 0;
}

