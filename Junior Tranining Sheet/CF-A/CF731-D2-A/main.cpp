#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int step(char a, char b) {
    int numB = static_cast<int> (b);
    int numA = static_cast<int> (a);
    return min(abs(numB-numA), 26 - abs(numB-numA));
}

int main()
{
    string s;
    cin >> s;
    int rota =  step('a', s[0]);
    for (int i = 0; i < s.size() -1; i++) {
        rota += step(s[i], s[i+1]);
    }
    cout << rota << endl;
    return 0;
}
