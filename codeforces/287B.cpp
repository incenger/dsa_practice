#include <iostream>
using namespace std;

long long cal(long long x, long long k) {
	return (k+x)*(k-x+1)/2;
}


int main() {
	long long n, k;
	cin >> n >> k;
	if (n == 1) {
		cout << 0;
		return 0;
	} else if (n - 1 > cal(1, k-1) ) {
		cout << -1;
		return 0;
	}
	long long l = 1, r = k-1;
	while (l < r) {
		long long mi = l + (r - l)/2;
		long long sum = cal(mi, k-1);
		if (sum > n-1) l = mi +1;
		else r = mi;
	}
	long long rem = n -1 - cal(l, k-1);
	long long ans = k -l;
	if (rem > 0) ans++;
	cout << ans;
	return 0;
}