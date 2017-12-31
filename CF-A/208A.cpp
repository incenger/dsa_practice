#include <iostream>

using namespace std;

int main()
{
    string s, t = "";
    cin >> s;
    bool isBetween  = false;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'W' && s[i+1] == 'U' && s[i+2] == 'B') {
            i+=2;
            if (isBetween)
                cout << " ";

        } else {
            cout <<s[i];
            isBetween = true;
        }
    }
    return 0;
}
