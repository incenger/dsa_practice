#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int anton = 0, danik = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'A')
            anton++;
        else
            danik++;
    }
    if (anton > danik)
        cout << "Anton" << endl;
    else if (anton < danik)
        cout << "Danik" << endl;
    else
        cout << "Friendship" << endl;
    return 0;
}
