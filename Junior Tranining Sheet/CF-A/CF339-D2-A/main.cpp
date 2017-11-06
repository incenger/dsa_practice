#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int a[100];
    int index = 0;
    for (int i = 0; i < s.size(); i+=2) {
            a[index++] = static_cast<int> (s[i] - '0');
    }
    sort(a, a + index);
    for (int i = 0;  i< index; i++) {
        cout << a[i];
        if (i!= index -1) {
            cout << "+";
        }
    }
    return 0;
}
