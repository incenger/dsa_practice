#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;

int gcd(int x, int y) {
    if (y == 0) return x;
    int r = x % y;
    return gcd (y, r);
}

int main()
{
    int x, y;
    while (cin >> x) {
        cin >> y;
        if (gcd(x, y) == 1) {
            printf("%10d%10d    %s\n\n", x, y, "Good Choice");
        } else {
            printf("%10d%10d    %s\n\n", x, y, "Bad Choice");
        }
    }
    return 0;
}
