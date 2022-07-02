#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct Node {
    string val;
    bool check;
    int assign;
};

int numberOfNodes;
map<unsigned long long, Node> nodes;

unsigned long long position(string p) {
    if (p == "") {
        nodes[0].check = true;
        return 0;
    }
           
    else if (p[p.size()-1] == 'L') {
        int pos =  position(p.substr(0, p.size()-1))*2 +1;
        nodes[pos].check = true;
        return pos;
    } else {
        int pos =  position(p.substr(0, p.size()-1))*2 +2;
        nodes[pos].check = true;
        return pos;

    }
}

void init() {
    nodes.clear();
    numberOfNodes = 0;
}

int main() {
    init();
    string s;
    while (cin >> s) {
        if (s == "()") {
            bool sat = true; 
            for (auto& node : nodes) {
                if (node.second.check) {
                    if (node.second.val == "" || node.second.assign > 1)
                    sat = false;
                }
            }

            if (!sat) {
                cout << "not complete" << endl;
            } else {
                for (auto& node : nodes) {
                    if (node.second.check) {
                        if (numberOfNodes > 1) cout << node.second.val << " ";
                        else cout << node.second.val << endl;
                        numberOfNodes--;
                    }
                }
            }
            init();
        } else {
            string val = s.substr(1, s.find(',') - 1);
            string path = s.substr(s.find(',') +1, s.size() -2 -s.find(','));
            unsigned long long pos = position(path);
            nodes[pos].val = val;
            nodes[pos].assign++;
            numberOfNodes++;
        }
    }
    return 0;
}
