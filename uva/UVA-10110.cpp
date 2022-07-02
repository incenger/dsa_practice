#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    unsigned int n;
    while (cin >> n && n != 0) {
        unsigned int x = sqrt(n);
        if (x*x == n)
            cout <<"yes" << endl;
        else
            cout <<"no" << endl;
    }
    return 0;
}
