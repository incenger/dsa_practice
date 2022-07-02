#include <iostream>
using namespace std;

bool isPrime(int n) {
	if (n == 1) return false;
	for (int i = 2; i*i <= n; i++) {
		if (n % i == 0) return false;
	}
	return true;
}

int nextPrime(int n) {
	int x = n+1;
	while(true) {
		if (isPrime(x)) return x;
		x++;
	}
}

int main() {
	int n, m;
	cin >> n >> m;
	if(nextPrime(n) == m) cout << "YES";
	else cout << "NO";
	return 0;
}