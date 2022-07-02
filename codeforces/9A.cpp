#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int m, int n) {
    m = abs(m);
    n = abs(n);
    if (n == 0)
        return m;
    return gcd(n, m%n);
}

int main()
{
    int a, b;
    cin >> a >> b;
    int chance =  6 - max(a, b) + 1;
    int nume = chance / gcd(chance, 6);
    int deno = 6 / gcd(chance, 6);
    cout << nume << "/" << deno << endl;
    return 0;
}
