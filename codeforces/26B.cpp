#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	stack<char> open;
	string s;
	int res = 0;
	cin >> s;
	for (int i = 0; i < s.length(); i++) {
		if(s[i] == '(') open.push('(');
		else  {
			if (!open.empty()) {
				open.pop();
				res++;
			}
		}
	}
	cout << res*2;
	return 0;
}