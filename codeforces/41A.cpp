#include <iostream>

using namespace std;

bool rever(string s, string t) {
    if (s.size() != t.size())
        return false;
    int sz = s.size();
    for (int i = 0; i < sz; i++) {
        if (s[i] != t[sz -1 -i])
            return false;
    }
    return true;
}

int main()
{
    string s, t;
    cin >> s >> t;
    if (rever(s, t))
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
