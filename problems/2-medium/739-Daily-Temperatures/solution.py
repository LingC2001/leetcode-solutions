from typing import List


def dailyTemperatures(self, temp: List[int]) -> List[int]:
    sols = [0] * len(temp)
    st = []

    for i in range(len(temp)):
        while st and temp[i] > temp[st[-1]]:
            prev = st.pop()
            sols[prev] = i - prev
        st.append(i)
    return sols
