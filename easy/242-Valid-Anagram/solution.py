def isAnagram(s: str, t: str) -> bool:
    dict_1 = {}
    dict_2 = {}

    for letter in s:
        if letter in dict_1:
            dict_1[letter] += 1
        else:
            dict_1[letter] = 0

    for letter in t:
        if letter in dict_2:
            dict_2[letter] += 1
        else:
            dict_2[letter] = 0

    return dict_1 == dict_2
