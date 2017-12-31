#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int a, b,c, d;
	cin >> a >> b >> c >> d;
	int m = max(c, d);
	int n = min(2*c, 2*d);
	if (n < m || a <= d || b <= d) cout << -1;
	else {
		int x = (m + n)/2;
		if (b <= 2*d) b  = b*2;
		if (a <= b) a = b +1;
		cout << a << " " << b << " " << x;
	}
	return 0;
}