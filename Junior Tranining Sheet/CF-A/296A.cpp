#include <iostream>
using namespace std;

int main() {
	int a[1001] = {0};
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		a[x]++;
	}
	int max = 0;
	for (int i = 1; i <= 1000; i++) {
		if (a[i]  > max) max = a[i]; 
	}
	if (2* max > (n + 1)) cout << "NO";
	else cout << "YES";
	return 0;
}