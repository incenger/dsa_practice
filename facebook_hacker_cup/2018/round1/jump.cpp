#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

const double epsilon = 10e-10;
const int INF = (int) 10e9;
vector<int> U;
vector<int> D;
vector<long long> H;
int N, M;

bool check(double x) {
    double lowb = (double)H[0]- x;
    double upb = (double)H[0] +x;
    for (int  i = 0; i < N-1; i++){
        upb = min(upb + U[i], H[i+1] + x);
        lowb = max(lowb - D[i], H[i+1]-x);
        if (lowb > upb) return false;
    }
    return true;
}

int main(int argc, char const *argv[])
{
    freopen("INPUT.TXT", "rt", stdin);
    freopen("OUTPUT.TXT", "wr", stdout);
    int T;
    cin >> T;
    for (int  t = 1; t <= T; t++){
        cin >> N >> M;
        H = vector<long long>(N);
        U = vector<int>(N, INF);
        D = vector<int>(N, INF);
        cin >> H[0] >> H[1];
        long long w, x, y, z;
        cin >> w >> x >> y >> z;
        for (int i = 2; i < N; i++) {
            H[i] = (w*H[i-2] + x*H[i-1] + y) % z;
        }
        for (int i = 0; i < M; i++) {
            int a, b, u, d;
            cin >> a >> b >> u >> d;
            a--; b--;
            if (b < a) {
                swap(a, b);
                swap(u, d);
            }
            for (int  j = a; j < b; j++) {
                U[j] = min(U[j], u);
                D[j] = min(D[j], d);
            }
        }
        double lo = 0;
        double hi = 1e7;
        while (lo + epsilon <  hi) {
            double mi = (lo + hi)/2;
            if (check(mi)) hi = mi;
            else lo = mi;
        }
        cout << "Case #" << t << ": "<< fixed << setprecision(6) << lo;
        if (t != T) cout << endl;
    }
    return 0;
}
