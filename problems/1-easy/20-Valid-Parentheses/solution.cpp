#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

bool isValid(string s) {
    unordered_map<char, char> mapping = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
    vector<char> stack = {};

    for (char c : s) {
        if (mapping.find(c) != mapping.end()) {
            stack.push_back(c);
        } else {
            if ((stack.size() > 0) && mapping[stack.back()] == c) {
                stack.pop_back();
            } else {
                return false;
            }
        }
    }

    return stack.size() == 0;
}
