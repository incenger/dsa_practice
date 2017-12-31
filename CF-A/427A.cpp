#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int crime = 0, free = 0;
    for (int i = 0; i < n; i++) {
        bool isCrime = false;
        int event;
        cin >> event;
        if (event < 0) {
            crime++;
            isCrime =true;
        }
        else
            free += event;
        if (free > 0 && isCrime) {
            crime--;
            free--;
        }
    }
    cout << crime << endl;
    return 0;
}
