#include <iostream>
#include <string>

using namespace std;

string s1 = "qwertyuiop";
string s2 = "asdfghjkl;";
string s3 = "zxcvbnm,./";

char shift(char c, char di) {
    if (di == 'R') {
        for (int i = 0; i < 10; i++) {
            if (c == s1[i]) {
                return s1[((i+10)-1) %10];
            }
            if (c == s2[i]) {
                return s2[((i+10)-1) %10];
            }
            if (c == s3[i]) {
                return s3[((i+10)-1) %10];
            }
        }
    } else if (di == 'L') {
        for (int i = 0; i < 10; i++) {
            if (c == s1[i]) {
                return s1[((i+10)+1) %10];
            }
            if (c == s2[i]) {
                return s2[((i+10)+1) %10];
            }
            if (c == s3[i]) {
                return s3[((i+10)+1) %10];
            }
        }
    }
}

int main()
{

    char c;
    cin >> c;
    string s;
    cin >> s;
    for (int i = 0;  i < s.size(); i++) {
        s[i] = shift(s[i], c);
    }
    cout << s << endl;
    return 0;
}
