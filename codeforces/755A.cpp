#include <bits/stdc++.h>

using namespace std;


int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    int res = -1;
    if (n == 2 || n == 1) {
        res = 7;
    } else if (n == 3) {
        res = 1;
    } else {
        res = n-2;
    }
    cout << res;
    return 0;
}
