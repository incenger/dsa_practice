#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int init = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            char c;
            cin >> c;
            if (c == '+') {
                init++;
                break;
            } else if (c == '-') {
                init--;
                break;
            }
        }
        cin.get();
    }
    cout << init << endl;
    return 0;
}
