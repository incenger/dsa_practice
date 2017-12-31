#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	cin >> s;
	if (s == "9") cout << 9;
	else {
		for (int i = 0; i < s.length(); i++) {
			if (s[i] > '4') {
				if (i == 0 && s[i] == '9') cout << s[i];
				else cout << (char)('9' - s[i] + '0');
			}
			else cout << s[i];
		}
	}
	
	return 0;
}