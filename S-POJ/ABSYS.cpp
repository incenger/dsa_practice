#include <iostream>
#include <algorithm>

using namespace std;

const string code = "machula";

int parseInt(string s) {
	int n = 0;
	for (int i = 0; i < s.length(); i++) {
		n = n*10 + (s[i] - '0');
	}
	return n;
}


int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin.get();
		int pos = 0;
		int index = 0;
		int a[2];
		for (int j = 0; j < 5; j++) {
			string s;
			cin >> s;
			if (j % 2 == 0) {
				if ( s.find(code) == string::npos) {
					a[index] = parseInt(s);
					index++;
				}  else {
					pos = j;
				}
			}
		}
		int res = 0;
		if (pos > 3) res = a[0] + a[1];
		else res = a[1] - a[0];
		if (pos == 0) cout << res << " + " << a[0] << " = " << a[1] << endl;
		else if (pos == 2) cout << a[0] << " + " << res << " = " << a[1] << endl;
		else cout << a[0] << " + " << a[1] << " = " << res << endl;
	}
	return 0;
}