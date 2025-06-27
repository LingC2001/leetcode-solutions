#include <vector>
#include <string>
#include <unordered_map>
#include <sstream> 

using namespace std;

string getSignature(const string& s) {
    vector<int> count(26, 0);
    for (char c : s) {
        count[c - 'a']++;
    }

    stringstream ss;
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) {
            ss << (char)('a' + i) << count[i];
        }
    }
    return ss.str();
}

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    vector<vector<string>> result;
    unordered_map<string, vector<string>> groups;

    for (const string& s : strs) {
        groups[getSignature(s)].push_back(s);
    }

    for (const auto& entry : groups) {
        result.push_back(entry.second);
    }

    return result;
}