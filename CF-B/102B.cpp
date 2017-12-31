#include <iostream>
using namespace std;

string  digit(string s) {
	int sum = 0;
	for (int i = 0; i < s.length(); i++) {
		sum += s[i] - '0';
	}
	return to_string(sum);
}

int main() {
	string s;
	cin >> s;
	int c = 0;
	while (s.length() > 1) {
		c++;
		s = digit(s);
	}
	cout << c;
	return 0;
}