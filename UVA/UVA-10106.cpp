#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int XY = 62500;

int main()
{
    string s,t;
    while (cin >> s) {
        cin >> t;
        int a[XY] = {0};
        reverse(s.begin(), s.end());
        reverse(t.begin(), t.end());
        for (int i = 0; i < s.length(); i++) {
            for (int  j = 0; j < t.length(); j++) {
                a[i+j] += (s[i] - '0')*(t[j]-'0');
            }
        }
        for (int i = 0; i < XY -1; i++) {
            a[i+1] += a[i]/10;
            a[i] %= 10;
        }
        int i = XY-1;
        while (i > 0 && a[i] == 0) i--;
        while (i>= 0) {
            cout << a[i];
            i--;
        }
        cout << endl;
    }
    return 0;
}
