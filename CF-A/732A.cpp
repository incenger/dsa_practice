#include <iostream>

using namespace std;

int main()
{
    int k, r;
    cin >> k >> r;
    int buy = 1;
    bool isNoChange = false;
    while (!isNoChange) {
        if (((buy * k) % 10 == 0) || (buy * k ) % 10 == r)
            isNoChange = true;
        else
            buy++;
    }
    cout << buy << endl;
    return 0;
}
