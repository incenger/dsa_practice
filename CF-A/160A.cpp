#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];
    int sum = 0;
    for (int i = 0;  i < n; i++) {
        cin >> a[i];
        sum +=  a[i];
    }
    sort(a, a+ n);
    int i = n-1;
    int coins = 0;
    while (coins*2 <= sum) {
        coins += a[i--];
    }
    cout << n - i -1 << endl;

    return 0;
}
