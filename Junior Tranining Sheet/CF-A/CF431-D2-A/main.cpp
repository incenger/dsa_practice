#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int a[4];
    for (int i = 0; i < 4; i++) {
        cin >> a[i];
    }
    string s;
    cin >> s;
    int calo = 0;
    for (int i = 0; i < s.size(); i++) {
        int num = static_cast<int> (s[i] - '0') - 1;
        calo += a[num%4];
    }
    cout << calo << endl;
    return 0;
}
