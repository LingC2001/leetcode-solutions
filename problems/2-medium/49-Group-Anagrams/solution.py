from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    seen_dict = {}
    res = []
    res_index = 0
    for string in strs:
        signature = [0] * 26
        for letter in string:
            signature[(ord(letter) - 97)] += 1

        hashable_signature = tuple(signature)

        if hashable_signature in seen_dict:
            res[seen_dict[hashable_signature]].append(string)

        else:
            seen_dict[hashable_signature] = res_index
            res_index += 1
            res.append([string])
    return res
