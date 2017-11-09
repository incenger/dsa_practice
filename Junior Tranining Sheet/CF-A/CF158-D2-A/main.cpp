#include <iostream>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int score = a[k-1];
    int pass = 0;
    while (a[pass] >= score && a[pass] > 0 && pass < n) {
        pass++;
    }
    cout << pass << endl;
    return 0;
}
