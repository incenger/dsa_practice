#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> a(4);
    int count = 0;
    for (int i = 0; i < 4; i++) {
        int n;
        cin >> n;
        if (find(a.begin(), a.end(), n) != a.end()) {
            count++;
        } else {
            a.push_back(n);
        }
    }
    cout << count << endl;
    return 0;
}
