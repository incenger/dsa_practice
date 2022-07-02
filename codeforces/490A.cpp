#include <iostream>

using namespace std;

int main()
{
    int n, team = 0;
    cin >> n;
    int pr[5000] = {0}, pe[5000] = {0}, m[5000] = {0};
    int i1= 0, i2 = 0, i3= 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x == 1) {
            pr[i1++] = i+1;
        } else if (x == 2) {
            m[i2++] = i+1;
        } else if (x == 3) {
            pe[i3++] = i+1;
        }
    }
    while(pr[team] != 0 && m[team] != 0 && pe[team] != 0) {
        team++;
    }
    cout << team << endl;
    for (int i = 0; i < team; i++) {
        cout << m[i] << " " << pe[i] << " " << pr[i] << endl;
    }
    return 0;
}
