#include <bits/stdc++.h>

using namespace std;

int main () {
    int n, s, m;
    cin >> n >> s;
    int min = s;
    for (auto i = 0; i < n; ++i) {
        cin >> m;
        s += m;
        if (s < min) {
            min = s;
        }
    }
    cout << min << '\n';
    return 0;
}