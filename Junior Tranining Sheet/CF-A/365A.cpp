#include <iostream>
#include <string>
using namespace std;

bool isKGood(string s, int k) {
	bool a[k+1] = {false};
	for (int i = 0; i < s.length(); i++) {
		a[s[i]- '0'] = true;
	}
	for (int i = 0; i <= k; i++) {
		if (a[i] == false) return false;
	}
	return true;
	
}


int main() {
	int n, k, count = 0;
	cin >> n >> k;
	while (n--) {
		string s;
		cin >> s;
		if (isKGood(s, k)) count++;
	}
	cout << count;
	return 0;
}