#include <iostream>
using namespace std;

int bigMod(unsigned int a,unsigned int b,unsigned int c) {
	if (b == 0) return 1;
	if (b % 2 == 0) {
		unsigned int x = bigMod(a, b/2, c);
		return (x*x) % c;
	}
	return ((a % c)*bigMod(a, b -1, c))%c;
}

int main() {
	unsigned int a, b, c;
	while (cin >> a >> b >> c) {
		cout << bigMod(a, b, c) << endl;
	}
	return 0;
}