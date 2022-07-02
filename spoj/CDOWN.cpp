#include <iostream>
#include <bits/stdc++.h>

using namespace std;

map<string, vector<string> > v;
map<string, int> p;

int t, n, d;

bool sortbysec(const pair<int,string> &a,
              const pair<int,string> &b)
{
    return (a.second < b.second);
}

bool sortbyfirst(const pair<int,string> &a,
              const pair<int,string> &b)
{
    return (a.first > b.first);
}

int calcHeight(string name) {
	if (p[name] >= 0) return p[name];
	vector<string> son = v[name];
	if(son.empty()) {
		return p[name] = 0;
		return 0;
	}
	int max = 0;
	for (int i = 0; i < son.size(); i++) {
		int h = calcHeight(son[i]);
		if (h > max) max = h;
		
	}
	p[name] = max + 1;
	return max + 1;
}

int countD(string origin, string name, int h) {
	if(p[origin] < d) return 0;
	if (h == d -1) return v[name].size();
	vector<string> son = v[name];
	int c = 0;
	for (int i = 0; i < son.size(); i++) {
		c += countD(origin, son[i], h+1);
	}
	return c;
}

void init() {
	cin >> n >> d;
	while(n--) {
		string parent;
		cin >> parent;
		p[parent] = -1;
		int x;
		cin >> x;
		vector<string> son;
		while(x--) {
			string s;
			cin >> s;
			son.push_back(s);
			p[s] = -1;
		}
		v[parent] = son;
	}
}					
				
			
	

int main() {
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++) {
		init();
		
		vector<pair<int , string>> res;
		map<string, vector<string>>::iterator it;
		for (it = v.begin(); it != v.end(); it++) {
			calcHeight(it->first);
		}
		for (it = v.begin(); it != v.end(); it++) {
			string name = it->first;
			vector<string> son = it->second;
			int count  = countD(name, name, 0);
			if (count) res.push_back(make_pair(count, name));
		}
		sort(res.begin(), res.end(), sortbysec);
		stable_sort(res.begin(), res.end(), sortbyfirst);
		int count  = res.size();
		cout << "Tree " << k << ":" << endl;
		if (count <= 3) {
			for (int i = 0; i < count; i++) {
				cout << res[i].second << " " << res[i].first << endl;
			}
		} else {
			int pivot = res[2].first ;
			if (res[3].first == pivot) {
				int i = 0;
				while(i < count && res[i].first >= pivot) {
					cout << res[i].second << " " << res[i].first << endl;
					i++;
				}
			} else {
				for (int i = 0; i < 3; i++) {
					cout << res[i].second << " " << res[i].first << endl;
				}
			}
		}
		cout << endl;
		v.clear();
		p.clear();
		
	}

	return 0;
}