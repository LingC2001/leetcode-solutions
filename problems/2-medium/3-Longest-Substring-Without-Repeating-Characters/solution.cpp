#include <string>
#include <unordered_set>

using namespace std;


int lengthOfLongestSubstring(string s) {
    unordered_set<char> substr_chars;
    int max_len = 0;
    int l = 0;
    int r = 0;
    while (r < s.size()) {
        while (substr_chars.find(s[r]) != substr_chars.end()) {
            substr_chars.erase(s[l]);
            l += 1;
        }
        substr_chars.insert(s[r]);
        r += 1;
        max_len = max(max_len, r-l);
    } 
    return max_len;
}
