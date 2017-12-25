#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    bool color = false;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            string s;
            cin >> s;
            if (s.compare("B") != 0 && s.compare("W") != 0 && s.compare("G") != 0)
                color = true;
        }
    }
    if (color)
        cout << "#Color";
    else
        cout << "#Black&White";
}
