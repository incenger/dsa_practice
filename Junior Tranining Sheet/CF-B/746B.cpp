#include <iostream>
#include <string>
using namespace std;

string encode (string s) {
	int le = s.length();
	string res;
	while (le > 0) {
		int mi = (le -1)/2;
		res += s[mi];
		s.erase(mi, 1);
		--le;
	}
	return res;
}

int main() {
	int n;
	cin >> n;
	string s;
	cin >> s;
	string t = s;
	while (encode(t) != s) t = encode(t);
	cout << t;
	return 0;
}