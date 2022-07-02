#include <iostream>

using namespace std;

int main()
{
    int n, b, d;
    cin >> n >> b >> d;
    int empty = 0;
    int waste = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x <= b) {
            waste += x;
            if (waste > d) {
                empty++;
                waste = 0;
            }
        }
    }
    cout << empty << endl;
    return 0;
}
