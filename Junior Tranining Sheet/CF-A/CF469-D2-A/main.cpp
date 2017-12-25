#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    bool pass[n+1] = {false};
    int p;
    cin >> p;
    for (int i = 0; i < p ;i++) {
        int x;
        cin >> x;
        pass[x] = true;
    }
    cin >> p;
    for (int i = 0; i < p ;i++) {
        int x;
        cin >> x;
        pass[x] = true;
    }
    bool passBoth = true;
    for (int i = 1; i <= n; i++) {
        if (!pass[i]) {
            passBoth = false;
            break;
        }
    }
    if (passBoth)
        cout << "I become the guy." << endl;
    else
        cout << "Oh, my keyboard!" << endl;
    return 0;
}
