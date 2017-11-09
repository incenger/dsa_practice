#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    if (n < 26)
        cout << "NO" << endl;
    else {
        char a[26] = {0};
        for (int i = 0; i < n; i++) {
            char c;
            cin >> c;
            a[static_cast<int> (tolower(c) - 'a')]++;
        }
        for (int i = 0; i < 26; i++) {
            if (a[i] == 0) {
                cout << "NO" << endl;
                return 0;
            }
        }
        cout << "YES" << endl;
    }

    return 0;
}
