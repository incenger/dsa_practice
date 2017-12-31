#include <iostream>
#include <cmath>
using namespace std;



int main()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    int zero = 0;
    int one = 0;
    for (int i= 0; i < n; i++) {
        if (s[i] == '0')
            zero++;
        else
            one++;
    }
    cout << abs(zero - one) << endl;
    return 0;
}
