#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int alpha[26] = {0};
    string s;
    char c;
    cin >> c;
    while (c!= '}') {
        if (isalpha(c))
            alpha[static_cast<int> (c - 'a')]++;
        cin >> c;
    }
    int dist = 0;
    for (int i = 0; i < 26; i++) {
        if (alpha[i] > 0)

            dist++;
    }
    cout << dist << endl;
    return 0;
}
