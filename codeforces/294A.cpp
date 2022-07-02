#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n;
    int a[n];
    for (int i = 0; i <  n; i++) {
        cin >> a[i];
    }
    cin >> m;
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        x = x -1;
        int left  = y -1;
        int right = a[x] - y;
        if (x == 0)
            a[x] -= left;
        else
            a[x-1] += left;

        if (x == n -1) {
            a[x] -= right;
        } else
            a[x+1] += right;
        a[x] = 0;
    }
    for (int i = 0; i < n; i++) {
        cout << a[i] << endl;
    }
    return 0;
}
