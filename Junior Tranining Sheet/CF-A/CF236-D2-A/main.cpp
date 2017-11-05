#include <iostream>
#include <vector>

using namespace std;

int main()
{
    char a[26];
    for (int i = 0; i < 26; i++) {
        a[i] = 0;
    }
    string s;
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        a[static_cast<int> (s[i] - 'a')]++;
    }
    int count = 0;
    for (int i = 0; i < 26; i++) {
        if (a[i] != 0)
            count++;
    }
    if (count % 2 == 0)
        cout << "CHAT WITH HER!" << endl;
    else
        cout << "IGNORE HIM!" << endl;
    return 0;
}
