#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n, t,k, d;
    cin >> n >> t >> k >> d;
    if ((d/t + 1)*k >= n)
        cout << "NO";
    else
        cout << "YES";
    return 0;
}
