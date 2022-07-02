#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    int k;
    cin >> s >> k;
    int i = 0;
    while (i < s.size()-1 && k > 0) {
        char c = s[i];
        int index = i;
        for (int j = i+1; j <= i + k && j < s.size(); j++) {
            if (s[j] > c) {
                c = s[j];
                index = j;
            }
        }
        for (int  j = index; j > i; j--) swap(s[j], s[j-1]);
        k-=(index - i);
        i++;
    }
    cout << s;
    
    return 0;
}
