#include <iostream>
#include <algorithm>
#define MAX 100005
using namespace std;

int main() {
	long long a[MAX];
	int n, x;
	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a+n);
	long long res = 0;
	for (int i = 0; i < n; i++) {
		res += a[i]*x;
		if (x > 1) x--;
	}
	cout << res;
	return 0;
}