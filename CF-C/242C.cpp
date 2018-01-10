#include <iostream>
#include <bits/stdc++.h>

using namespace std;

set<pair<int, int> > allowed;
map<pair<int, int>, int> cell;
pair<int, int> start, final;

int moveX[] = {0, -1 , -1, -1, 0, 1, 1, 1};
int moveY[] = {1, 1, 0, -1, -1, -1, 0, 1};

int sol() {
	queue<pair<int ,int>> q;
	cell[start] = 0;
	q.push(start);
	while (!q.empty()) {
		pair<int, int> current = q.front();
		q.pop();
		if (current == final) return cell[current];
		for (int i = 0; i < 8; i++) {
			int nextX = current.first + moveX[i];
			int nextY = current.second + moveY[i];
			pair<int, int> next{nextX, nextY};
			if (allowed.count(next) && cell[next] == 0) {
				cell[next] = cell[current] +1;
				q.push(next);
			}
		}
	}
	return -1;
}
	


int main() {
	int x0,y0, x1, y1, n;
	cin >> x0 >> y0 >> x1 >> y1;
	start = make_pair(x0, y0);
	final = make_pair(x1, y1);
	cin >> n;
	for (int i = 0; i < n; i++) {
		int r, a, b;
		cin >> r >> a >> b;
		for (int j = a; j <= b; j++) {
			allowed.insert(make_pair(r, j));
		}
	}
	cout << sol();
	return 0;
}