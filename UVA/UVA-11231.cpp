#include <iostream>

using namespace std;

int main()
{
    int x, y, z;
    while (cin >> x) {
        cin >> y;
        cin >> z;
        int board = (x-7)*(y-7)/2;
        if (x == 0 && y == 0 && z == 0)
            break;
        if (z == 0) {
            cout << board << endl;
        } else {
            cout << (x-7)*(y-7) - board << endl;
        }
    }
    return 0;
}
