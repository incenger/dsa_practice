#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    string a;
    cin >> a;
    int same = 0;
    for (int i = 0; i < n-1; i++) {
        if (a[i] == a[i+1])
            same++;
    }
    cout << same << endl;
    return 0;
}
