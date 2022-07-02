#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s, t;
    cin >> s;
    cin >> t;
    if (s.compare(t) == 0)
        cout << -1;
    else
        cout << max(s.size(), t.size());
    return 0;
}
