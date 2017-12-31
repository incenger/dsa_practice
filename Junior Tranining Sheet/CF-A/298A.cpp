#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;
	string a;
	cin >> a;
	int l = 0, r = 0, s, t;
	for (int i = 0; i < n; i++) {
		if (a[i] == 'L' || a[i] == 'R') {
			s = i+1;
			break;
		}
	}
	bool left = false;
	for (int i = 0; i < n; i++) {
		if (a[i] == 'L') {
			t = i;
			left = true;
			break;
		}
	}
	if (left) cout << s << " " << t;
	else {
		for (int i = n -1; i >= 0; i--) {
			if (a[i] == 'R') {
				t = i+2;
				break;
			}
		}
		cout << s << " " << t; 
	}
	return 0;
}