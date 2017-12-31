#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    string s1, s2;
    cin >> s1;
    int score =1;
    for (int i = 1; i < n; i++) {
        string t;
        cin >> t;
       if (s1.compare(t) == 0)
            score++;
       else s2 = t;
    }
    if (2*score > n)
        cout << s1;
    else
        cout << s2;
    return 0;
}
