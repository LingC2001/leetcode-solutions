#include <string>
using namespace std;

bool isPalindrome(string s) {
    string filtered = "";
    for (char c : s) {
        if (isalnum(c)) {
            filtered.push_back(tolower(c));
        }
    }

    int start = 0;
    int end = filtered.size()-1;
    while (start < end) {
        if (filtered[start] != filtered[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}
