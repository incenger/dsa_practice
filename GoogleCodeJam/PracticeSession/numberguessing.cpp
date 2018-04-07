#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--) {
        int a, b, n;
        cin >> a >> b >> n;
        ++a;
        string s;
        while (true) {
            int guess = a + (b-a)/2;
            cout << guess << endl;
            cin >> s;
            if (s == "CORRECT") break;
            else if (s == "TOO_SMALL") a = guess +1;
            else if (s == "TOO_BIG") b = guess -1;
        }
    }
    return 0;
}
