#include <iostream>
using namespace std;



int main() {
	int a[100000], q[100001];
	int n, m;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		q[a[i]] = i+1;
	}
	cin  >> m;
	long long v = 0, p = 0;
	for (int i = 0; i < m; i++) {
		int x;
		cin >> x;
		v += q[x];
		p += n -q[x] + 1;
	}
	cout << v << " " << p;
	

	return 0;
}