#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a%b);
}

int main() {
	int a[50];
	int t;
	while (true) {
		cin >> t;
		if (t == 0) break;
		for (int i = 0; i < t; i++) {
			cin >> a[i];
		}
		int pair = t*(t-1)/2;
		int count  = 0;
		for (int i = 0; i < t -1; i++) {
			for (int j = i+1; j < t; j++) {
				if (gcd(a[i], a[j]) == 1) count++;
			}
		}
		if (count  == 0) cout << "No estimate for this data set." << endl;
		else {
			double pi = sqrt(6.0*pair/count);
			cout << setprecision(6) << fixed << pi << endl;
		}
	}
	return 0;
}