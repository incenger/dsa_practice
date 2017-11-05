#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int turn = 0;
    int sereja = 0, dima = 0;
    int left = 0, right = n-1;
    while (left <= right) {
        turn++;
        int choice = max(a[left], a[right]);
        if (turn % 2 == 1)
            sereja += choice;
        else
            dima += choice;
        if (choice == a[left])
            left++;
        else
            right--;
    }
    cout << sereja << " " << dima << endl;
    return 0;
}
