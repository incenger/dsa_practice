#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void cal(string s, string t) {
	string res;
	int maxl = max(s.length(), t.length());
	while (s.length() < maxl ) s = s + '0';
	while (t.length() < maxl ) t = t + '0';
	int carry = 0;
	for (int i = 0; i < s.length(); i++) {
		int temp = s[i] -'0' + t[i] - '0' + carry;
		carry = temp/10;
		temp = temp % 10;
		res += (char) (temp + '0');
	}
	while (carry > 0) {
		int temp = carry % 10;
		carry /= 10;
		res += (char) temp + '0';
	}
	while (res[0] == '0') res.erase(0, 1);
	cout << res << endl;
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		string s, t;
		cin >> s >> t;
		cal(s, t);
	}
	return 0;
}