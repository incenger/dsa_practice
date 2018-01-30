#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    bool c[26];
    int questionmark;
    if (s.length() < 26) {cout << -1; return 0;}
    int l = s.length();
    bool found = false;
    for (int i = 0; i <= l -26; i++) {
        memset(c, false, sizeof(c));
        questionmark = 0;
        for (int j = i; j < i +26; j++) {
            if (s[j] == '?') questionmark++;
            else c[s[j] - 'A'] = true;
        }
        int have = 0;
        for (int j = 0; j < 26; j++) {
            if (c[j]) have++;
        }
        if (have + questionmark == 26) {
            for (int j =i; j < i + 26; j++) {
                if (s[j] == '?') {
                    for (int k = 0; k < 26; k++) {
                        if (!c[k]) { 
                            s[j] = 'A' + k;
                            c[k] =  true;
                            break;
                        }
                    }
                }
            }
            found =  true;
            break;
        }
    }
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '?') s[i] = 'X';
    }
    if (found) cout << s;
    else cout << -1;
    return 0;
}
