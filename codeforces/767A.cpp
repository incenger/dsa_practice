#include <iostream>


using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    bool has[n+1] = {false};
    int fin = n;
    for (int i = 0; i < n; i++) {
        has[a[i]] = true;
        while (has[fin] && fin > 0) {
            cout << fin << " ";
            fin--;
        }
        cout << endl;
    }
    return 0;
}

