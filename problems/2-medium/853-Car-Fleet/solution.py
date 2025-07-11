from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    zipped = sorted(zip(position, speed), reverse = True)
    time = []
    fleets = []
    prev_time = 0

    for p, s in zipped:
        time.append((target - p)/ s)

    for fleet_time in time:
        if fleet_time > prev_time:
            fleets.append(fleet_time)
            prev_time = fleet_time

    return len(fleets)
