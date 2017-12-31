#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>

#define MAX 10e9
using namespace std;

vector<int> a;
int n, l;
double sol() {
	double lo = 0;
	double hi = MAX;
	double mi;
	for (int i = 0; i < 1000; i++) {
		mi = (lo + hi)/2;
		//cout << mi << endl;
		double le = a[0] - mi;
		bool light = true;
		double ri = a[n-1] + mi;
		for (int j = 0; j < n -1; j++) {
			if (a[j] + mi < a[j+1] - mi) {
				light = false;
				break;
			}
		}
		if (light && le <= 0 && ri >= l) {
			hi = mi;
		} else lo = mi;
	}
	return mi;
}


int main() {
	cin >> n >> l;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		a.push_back(x);
	}
	sort(a.begin(), a.end());
	cout << setprecision(9) << fixed << sol();
	return 0;
}