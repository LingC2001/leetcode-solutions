from collections import defaultdict


def isAnagram(self, s: str, t: str) -> bool:
    dict_1 = defaultdict(int)
    for letter in s:
        dict_1[letter] += 1

    for letter in t:
        dict_1[letter] -= 1

    for count in dict_1.values():
        if count != 0:
            return False

    return True
