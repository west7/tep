#include <bits/stdc++.h>

using namespace std;

int main () {
    int n, p, d = 1, q = 1, di = 0;
    cin >> n >> p;
    while (true) {
        d =  q * p;
        q = d;
        if (d > n) {
            cout << di << '\n';
            break;
        }
        di++; 
    }
    return 0;
}