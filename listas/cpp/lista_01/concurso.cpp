#include <bits/stdc++.h>

using namespace std;

int main () {
    int n, k, a;  
    cin >> n >> k;
    vector<int> ns(n);
    for (auto i = 0; i < n; ++i) {
        cin >> a;
        ns.emplace_back(a);
    }
    sort(ns.begin(), ns.end(), greater<int>());
    cout << ns[--   k] << '\n';
    return 0;
}