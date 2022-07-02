#include <iostream>
#include <vector>
#define MAX 150005
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	int a[MAX], dp[MAX];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	int s = 0;
	for (int i = 0; i < k; i++) {
		s+= a[i];
	}
	dp[0] = s;
	for (int i = 1; i <= n - k; i++) {
		dp[i] = dp[i-1] - a[i-1] + a[i + k -1];
	}
	int min = s, res = 0;
	for (int i = 0; i <= n-k; i++) {
		if (dp[i] < min) {
			min = dp[i];
			res = i;
		}
	}
	cout << res +1;
	return 0;
}