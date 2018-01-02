#include <iostream>
#include <string>

using namespace std;

string num;

bool onlynine(string s) {
	for (int i = 0;  i< s.length(); i++) {
		if (s[i] != '9') return false;
	}
	return true;
}

void sol_nine() {
	cout << 1;
	for (int i = 0; i < num.length() -1; i++) cout <<  0;
	cout << 1 << endl;
}

int cmp() {
	int left;
	int right;
	if (num.length() % 2 == 0) {
		left = num.length()/2 -1;
		right = num.length()/2;
	} else {
		left = right = num.length()/2;
	}
	while (left >= 0) {
		if (num[left] > num[right]) return 1;
		else if (num[left] < num[right]) return -1;
		else {
			left--;
			right++;
		}
	}
	return 0;
}

void copy() {
	int l = num.length();
	for (int i = 0; i <= (l -1)/2; i++) {
		num[l-1-i] = num[i];
	}
}

void panli() {
	int i = (num.length() -1)/2;
	int d = num[i] - '0' + 1;
	while (d>= 10 && i > 0) {
		num[i] = '0';
		i--;
		d = num[i] - '0' + 1;
	}
	num[i] = (char) (d + '0');
	copy();
}

void sol() {
	int compar = cmp();
	if (compar > 0) copy();
	else panli();
	cout << num << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> num;
		if (onlynine(num)) sol_nine();
		else sol();
	}
	return 0;
}