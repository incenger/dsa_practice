#include <iostream>
#include <string>

using namespace std;

void sol(string s) {
    if (s.size() > 10) {
        cout << s[0] << s.size() -2 << s[s.size()-1] << endl;
    } else {
        cout << s << endl;
    }
}

int main()
{
    int n;
    cin >> n;
    string s[n];
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < n; i++) {
        sol(s[i]);
    }
    return 0;
}
