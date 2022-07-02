#include <iostream>
#include <bits/stdc++.h>
#include <cmath>

using namespace std;

int square(int x, int y, int a) {
    if (y < 0 || y % a == 0) return -1;
    int h = y/a;
    if (h == 0) {
        if (abs(x) < (a+1)/2) return 1;
        else return -1;
    }
    if (h % 2 == 1) {
        if (abs(x) < (a+1)/2) return h + (h-1)/2 + 1;
        else return -1;
    }
    if (h % 2 == 0) {
        if (abs(x) < a) {
            if (x > 0) return h + (h-1)/2 +2; 
            if (x < 0) return h + (h-1)/2 +1;
        }
        return -1;
    }
}


int main() {
    int a, x, y;
    cin >> a >> x >> y;
    cout << square(x, y, a);
    return 0;
}
