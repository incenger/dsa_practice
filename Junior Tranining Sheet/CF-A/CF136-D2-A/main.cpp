#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int give[n], receive[n];
    for (int i = 0; i < n; i++) {
        cin >> give[i];
    }
    for (int i = 0; i < n; i++) {
        receive[give[i] -1] = i+1;
    }
    for (int i = 0; i < n; i++) {
        cout << receive[i] << " ";
    }
    return 0;
}
