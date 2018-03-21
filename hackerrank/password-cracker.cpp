#include <bits/stdc++.h>

using namespace std;



bool matchPassword(vector<string> &pass, string attempt, vector<string> &index,  int begin, vector<bool>& dp) {
    if (begin >= attempt.size()) return true;
    
    if (!dp[begin]) return false;
    
    for (int i = 0; i < pass.size(); i++) {
        if (begin + pass[i].size() > attempt.size()) continue;
        string cmp = attempt.substr(begin, pass[i].size());
        if (cmp == pass[i]) {
            index.push_back(pass[i]);
            if (matchPassword(pass, attempt, index, begin + pass[i].size(), dp)) return true;
            else index.pop_back();
        }
    }
    dp[begin] = false;
    return false;
    
}

void passwordCracker(vector<string> &pass, string attempt, vector<string> &index, vector<bool>& dp) {
    if (matchPassword(pass, attempt, index, 0, dp)) {
        for (int i = 0; i < index.size(); i++)
            if (i!= index.size() -1) cout << index[i] << " ";
            else cout << index[i];
        cout << endl;
    } else cout << "WRONG PASSWORD" << endl;
}

int main() {
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        vector<string> index;
        vector<string> pass(n);
        
        
        for(int pass_i = 0; pass_i < n; pass_i++){
           cin >> pass[pass_i];
        }
        string attempt;
        cin >> attempt;
        vector<bool> dp(attempt.size());
        for (int i = 0; i < dp.size(); i++) dp[i] = true;
        passwordCracker(pass, attempt, index, dp);
    }
    return 0;
}
