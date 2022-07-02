#include <iostream>
#include <iomanip>
using namespace std;
const double PI = 3.14159265359;

int main() {
	int d, h, v, e;
	cin >> d >> h >> v >> e;
	double r = 1.0*d/2;
	double drink = v/(PI *r*r) - e;
	if (drink <= 0) cout << "NO" << endl;
	else {
		cout << "YES" << endl;
		cout << setprecision(12) << fixed << h /drink<< endl;
	}
	return 0;
}