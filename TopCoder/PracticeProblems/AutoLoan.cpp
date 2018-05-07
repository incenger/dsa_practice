#include <iostream>
#include <bits/stdc++.h>
#include <iomanip>
#include <cmath>

using namespace std;

class AutoLoan {
    private:
        double eps = 1e-9;

    public:
        double interestRate(double price, double mpay, int lterm) {
            double lo = 0;
            double hi = 100;
            double rate = 0;
            for (int i = 0; i < 100; i++) {
                double mid = (lo+hi)/2;
                rate = mid/100;
                double money = price*pow((1+rate), lterm) - mpay*(pow((1+rate), lterm) -1)/rate;
                cout << money << endl;
                if (money > 0) hi = mid;
                else if (money < 0) lo = mid;
                else return rate*1200;
            }
            return rate*1200;
        }

};

int main(int argc, char const* argv[]) {
    AutoLoan al;
    int price, pay, n;
    cin >> price >> pay >> n;
    cout << fixed << setprecision(8) << al.interestRate(price, pay, n) << endl;
    return 0;
}

