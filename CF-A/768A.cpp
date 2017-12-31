#include <iostream>

using namespace std;

int maxElement(int a[], int sz) {
    int m = a[0];
    for (int i = 0; i < sz; i++) {
        if (a[i] > m)
            m = a[i];
    }
    return m;

}
int minElement(int a[], int sz) {
    int m = a[0];
    for (int i = 0; i < sz; i++) {
        if (a[i] < m)
            m = a[i];
    }
    return m;

}

int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int c = 0;
    int m = maxElement(a, n);
    int p = minElement(a, n);
    for (int i = 0; i < n; i++) {
        if (a[i] != m && a[i] != p)
            c++;
    }
    cout << c << endl;
    return 0;
}
