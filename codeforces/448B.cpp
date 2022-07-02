#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool automaton(string s, string t) {
    int i = 0, j = 0;
    int sl = s.length(), tl = t.length();
    while(i < sl) {
        if (s[i] == t[j]) {
            i++;
            j++;
        }
        else i++;
    }
    return (j == tl);
}

int main() {
    string s, t;
    cin >> s >> t;
    if (automaton(s,t)) {
        cout << "automaton";
    } else {
        int cs[26] = {0};
        int ct[26] = {0};
        for (int i = 0; i < s.length(); i++) {
            cs[s[i]-'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            ct[t[i]-'a']++;
        }

        bool anagram = true;
        for (int i = 0; i < 26; i++) {
            if (cs[i] != ct[i]) anagram = false;
        }

        bool trans = true;
        for (int i = 0; i < 26; i++) {
            if (ct[i] > cs[i]) trans = false;
        }

        if (anagram) cout << "array";
        else if (trans) cout << "both";
        else cout << "need tree";
    }
    return 0;
}
