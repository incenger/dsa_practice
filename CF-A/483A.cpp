#include <iostream>
using namespace std;

int main() {
	unsigned long long l, r;
	cin >> l >> r;
	if (l%2 == 0) {
		if (r - l < 2) cout << -1;
		else cout << l <<" "<<  l + 1 << " " << l + 2 << endl;
	} else {
		if (r - l < 3) cout << -1;
		else cout << l + 1 <<" "<<  l + 2 << " " << l + 3 << endl;
	}
	
	return 0;
}