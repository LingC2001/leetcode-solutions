#include <vector>
#include <algorithm>
using namespace std;


int carFleet(int target, vector<int>& position, vector<int>& speed) {
    // create a pair of position and time to reach target
    vector<pair<int, double>> pos_time;
    // populate pair vector
    for (int i = 0; i < position.size(); i++) {
        double time = double(target-position[i])/double(speed[i]);
        pos_time.push_back({position[i], time});
    }
    
    // sort to get the car at the front to be at the front of vector
    auto cmp = [](pair<int, double> a, pair<int, double> b) {return a.first > b.first; };
    sort(pos_time.begin(), pos_time.end(), cmp);

    // calculate number of fleets, starting from front car:
    //  - if previous car catches up then it is same fleet
    //  - if previous car doesn't catch up, then it must be different fleet
    int fleets = 1;
    double current_fleet_time = pos_time[0].second;
    
    for (int i = 1; i < pos_time.size(); i++) {
        if (pos_time[i].second > current_fleet_time) {
            fleets++;
            current_fleet_time = pos_time[i].second;
        }
    }

    return fleets;
}
