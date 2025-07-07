from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        left = 0
        right = len(s1)

        # add letters for s1 dict comparison and setup for s2
        for i in range(len(s1)):
            s2_dict[s2[i]] += 1
            s1_dict[s1[i]] += 1

        # check if the setup already is the solution
        if s1_dict == s2_dict:
            return True

        while right < len(s2):
            # add the next letter to the right to s2
            s2_dict[s2[right]] += 1
            # remove the next letter from the left from s2
            s2_dict[s2[left]] -= 1

            # remove 0's from the dict for comparison with s1
            if s2_dict[s2[left]] == 0:
                s2_dict.pop(s2[left])

            if s1_dict == s2_dict:
                return True
            left += 1
            right += 1

        return False
