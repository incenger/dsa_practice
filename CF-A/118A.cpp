#include <iostream>
#include <stdlib.h>

using namespace std;

bool isVowel(char c) {
    return (  c == 'a' || c == 'o'
        ||c == 'e' || c == 'u'
        ||c == 'i' || c == 'y');
}

int main()
{
    string s;
    cin >> s;
    string result = "";
    for (int i =0; i < s.size(); i++) {
        s[i] = tolower(s[i]);
    }
    for (int i = 0; i <s.size(); i++) {
        if(!isVowel(s[i])) {
            result = result + "." + s[i];
        }
    }
    cout << result << endl;

    return 0;
}
