#include <iostream>

using namespace std;

int main()
{
    long long n, k;
    cin >> n >> k;
    long long odd = (n+1)/2;
    if (k <= odd)
        cout << k*2 -1 << endl;
    else
        cout << (k-odd)*2 << endl;

    return 0;
}
