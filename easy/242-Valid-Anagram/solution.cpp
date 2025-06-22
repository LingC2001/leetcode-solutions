#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> counter;
        for (char c : s) {
            if (counter.find(c) != counter.end()) {
                counter[c] += 1;
            } else {
                counter[c] = 1;
            }
        }

        for (char c : t) {
            if (counter.find(c) != counter.end()) {
                counter[c] -= 1;
                if (counter[c] <= 0) {
                    counter.erase(c);
                }
            } else {
                return false;
            }
        }

        if (counter.empty()) {
            return true;
        }

        return false;
        
    }
};