#include <iostream>
using namespace std;

int main() {
	long long n, m;
	cin  >> n >> m;
	long long min, max;
	long long p = n/m;
	long long q = n % m;
	max = ((m-1) + (n-m+1)*(n-m+1) -n)/2;
	min = (q*(p+1)*(p+1) + (m-q)*p*p - n)/2;
	cout << min << " " << max;
	return 0;
}