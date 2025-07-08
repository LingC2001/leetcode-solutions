#include <vector>
#include <string>
#include <unordered_set>
using namespace std;


int evalRPN(vector<string>& tokens) {
    vector<int> stack;
    unordered_set<string> operators = {"+", "-", "*", "/"};

    for (string s : tokens) {
        if (operators.find(s) != operators.end()) {
            int right = stack.back();
            stack.pop_back();
            int left = stack.back();
            stack.pop_back();

            if (s == "+") {
                stack.push_back(left + right);
            } else if (s == "-") {
                stack.push_back(left - right);
            } else if (s == "*") {
                stack.push_back(left * right);
            } else {
                stack.push_back(left / right);
            }
        } else {
            stack.push_back(stoi(s));
        }
    }
    return stack.back();
}
