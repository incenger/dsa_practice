#include <iostream>

using namespace std;

int main()
{
    int n, k;
    cin >> n >>k;
    char a[26];
    for (int i = 0; i < 26; i++) {
        a[i] = static_cast<char> (i) +'a';
    }
    for (int i = 0; i < n; i++) {
        cout << a[i % k];
    }
    return 0;
}
