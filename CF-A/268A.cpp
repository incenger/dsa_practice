#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];
    int h[n];
    int count = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i] >> h[i];
    }
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            if (a[i] == h[j])
                count++;
            if (a[j] == h[i])
                count++;
        }
    }
    cout << count << endl;
    return 0;
}
