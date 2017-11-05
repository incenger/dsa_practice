#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    int year = 0;
    while (a <= b) {
        year++;
        a*=3;
        b*=2;
    }
    cout << year << endl;
    return 0;
}
