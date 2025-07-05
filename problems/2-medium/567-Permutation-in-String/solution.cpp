#include <unordered_map>
#include <string>
using namespace std;


bool checkInclusion(string s1, string s2) {
    if (s1.length() > s2.length()) {
        return false;
    }

    unordered_map<char, int> counts;
    unordered_map<char, int> s1_count;
    // increase window to s1.length()
    for (int i = 0; i < s1.length(); i++) {
        s1_count[s1[i]] += 1;
        counts[s2[i]] += 1;
    }
    if (counts == s1_count) {
        return true;
    } 

    int l = 0;
    int r = s1.length();
    while (r < s2.length()) {
        // calculate new window counts
        counts[s2[l]] -= 1;
        if (counts[s2[l]] == 0 ) {
            counts.erase(s2[l]);
        }
        counts[s2[r]] += 1;
        
        // check if counts are same
        if (counts == s1_count) {
            return true;
        }
        // shift window
        l++;
        r++;
    }
    return false;
}
