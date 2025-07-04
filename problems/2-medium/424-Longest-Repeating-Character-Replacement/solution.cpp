#include <vector>
#include <string>

using namespace std;

int getCharIndex(char c);
int characterReplacement(string s, int k);


int characterReplacement(string s, int k) {
    vector<int> char_counts(26);
    int l = 0;
    int r = 0;
    int max_length = 0;
    int max_freq = 0;

    while (r < s.size()) {
        // increment s[r] count
        int curr_char_idx = getCharIndex(s[r]);
        char_counts[curr_char_idx] += 1;
        // finding char with max freq
        max_freq = max(max_freq, char_counts[curr_char_idx]);

        // satisfy condition + calculate length
        int length = r-l+1;
        while ((length - max_freq) > k)  {
            char_counts[getCharIndex(s[l])] -= 1;
            l += 1;
            length -= 1;
        }
        max_length = max(max_length, length);
        r += 1;
    }
    return max_length;
}

int getCharIndex(char c) {
    return int(c) - int('A');
}
