#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
#include <iomanip>
using namespace std;

int cal(int n, int k) {
	double res = 1;
	for (int i =0; i < k; i++) {
		res *= 1.0*(n-i)/(i+1);
	}
	return (int) res;
}

int main() {
	string s1,s2;
	cin >> s1;
	cin >> s2;
	int origin = 0, wifi = 0, unreco = 0;
	for (int i = 0; i < s1.length(); i++) {
		if (s1[i] == '+') origin++;
		else origin--;
		if (s2[i] == '+') wifi++;
		else if (s2[i] == '-') wifi--;
		else unreco++;
	}
	double res = 0;
	int dis = abs(origin - wifi);
	if(unreco == 0) {
		if (dis == 0) res = 1;
		else res = 0;
	}
	else if ((dis + unreco) % 2 != 0 || dis > unreco) res = 0;
	else {
		res = cal( unreco, (dis+unreco)/2) / pow(2, unreco);
	}
	cout << setprecision(12) << fixed << res;

	return 0;
}