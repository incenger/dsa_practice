#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    int l = s.length();
    //3 loops
    for (int i = 0; i < l; i++) {
        int x = s[i] - '0';
        if (x % 8 == 0) {
            cout << "YES" << endl;
            cout << x;
            return 0;
        }
    }
    for (int i = 0; i < l -1; i++) {
        for (int ii = i +1; ii < l; ii++) {
            int x = (s[i] - '0')*10 + (s[ii] - '0');
            if (x % 8 == 0) {
                cout << "YES" << endl;
                cout << x;
                return 0;
            }
        }
    }

    for (int i = 0; i < l -2; i++) {
        for (int ii = i + 1; ii < l - 1; ii++) {
            for (int iii = ii +1; iii < l; iii++) {
                int x = (s[i]-'0')*100 + (s[ii] - '0')*10 + (s[iii] - '0');
                if (x % 8 == 0) {
                    cout << "YES" << endl;
                    cout << x;
                    return 0;
                }
            }
        }
    }
    cout << "NO";
    return 0;
}





