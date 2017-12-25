#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
	int a[100][2];
	int n, k;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> a[i][0] >> a[i][1];
	}
	double sum = 0;
	for (int i = 1; i < n; i++) {
		double dist = pow((a[i][0] - a[i-1][0]), 2) + pow((a[i][1] - a[i-1][1]), 2);
		sum += sqrt(dist);
	}
	cout << setprecision(9) << fixed << sum * k /50 << endl;
	return 0;
}