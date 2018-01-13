#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int vp, vd, t, f, c, res = 0;
	cin >> vp >> vd >> t >> f >> c;
	double xp = t*vp, xd = 0;
	if (vp >= vd) {
		cout << 0;
		return 0;
	}
	while(true) {
		double chase = 1.0*xp/(vd-vp);
		xd = chase*vd;
		if(xd >= c) break;
		else {
			res++;
			xp += (f+chase*2.0)*vp;
		}
	}
	cout << res;
	return 0;
}