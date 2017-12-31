#include <iostream>

using namespace std;

bool rated(int a[], int b[], int sz) {
    for (int i = 0;  i< sz; i++) {
        if (a[i] != b[i])
            return true;
    }
    return false;
}

bool maybe(int a[], int sz) {
    for (int i = 0; i < sz -1; i++) {
        if (a[i] < a[i+1])
            return false;
    }
    return true;
}


int main()
{
    int n;
    cin >> n;
    int before[n], after[n];
    for (int i = 0; i < n; i++) {
        cin >> before[i] >> after[i];
    }
    if (rated(before, after, n))
        cout << "rated" << endl;
    else if (maybe(after, n))
        cout << "maybe" << endl;
    else
        cout << "unrated" << endl;
    return 0;
}
