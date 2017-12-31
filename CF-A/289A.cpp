#include <iostream>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	int values = 0;
	while (n--) {
		int l, r;
		cin >> l >> r;
		values += r - l +1;
	}
	cout << (k - (values %k )) % k;
	return 0;
}