#include <iostream>

using namespace std;

int cal(int a[], int sz) {
    int s = 0;
    for (int i = 0; i < sz; i++) {
        s += a[i];
    }
    return s;
}

int main()
{
    int n;
    cin >> n;
    int x[n], y[n], z[n];
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i] >> z[i];
    }
    if (cal(x, n)  == 0 && cal(y, n) == 0 && cal(z, n) == 0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
