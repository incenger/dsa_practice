#include <iostream>

using namespace std;

int main()
{
    int n;
    long long x;
    cin >> n >> x;
    int distress = 0;
    for (int i = 0;  i < n; i++) {
        char c;
        cin >> c;
        if (c == '+') {
            int a;
            cin >> a;
            x += a;
        } else if (c == '-') {
            int a;
            cin >> a;
            if ( a > x) {
                distress++;
            } else {
                x -= a;
            }
        }
    }
    cout << x << " " << distress << endl;
    return 0;
}
