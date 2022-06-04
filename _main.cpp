#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
typedef long long ll;

using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);  // !!!!!!!!!!!

    int n, x, l, r, maxim, now = 0, tim = 0, last = 1, first = 0;
    cin >> n >> x;
    vector<pair<int, int>> time;
    for (int i = 0; i < n; ++i) {
        cin >> l >> r;
        time.emplace_back(l, r);
    }
    sort(time.begin(), time.end());

    for (int i = 0; i < n; ++i) {
        last = i;
        now++;
        tim = time[last].second - time[first].first;
        if (tim > x){
            first++;
            now--;
        }
        maxim = max(now, maxim);

    }
    cout << maxim;
}