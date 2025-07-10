#include <vector>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    vector<int> idx_stack;
    vector<int> res(temperatures.size(), 0);

    for (int curr_day = 0; curr_day < temperatures.size(); curr_day++) {
        int curr_temp = temperatures[curr_day];
        while (!idx_stack.empty() && (curr_temp > temperatures[idx_stack.back()]) ) {
            int day_idx = idx_stack.back();
            res[day_idx] = curr_day-day_idx;
            idx_stack.pop_back();
        }
        idx_stack.push_back(curr_day);
    }

    return res;
}
