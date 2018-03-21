#include <bits/stdc++.h>

using namespace std;

int digitSum(string n, int k) {
    long long sum  = 0;
    for (int i = 0; i < n.size(); i++)
        sum = (sum + (n[i]-'0')) % 9;
    return ((k%9)*sum)%9;
}

int main() {
    string n;
    int k;
    cin >> n >> k;
    int result = digitSum(n, k);
    cout << (result == 0 ? 9 : result) << endl;
    return 0;
}

