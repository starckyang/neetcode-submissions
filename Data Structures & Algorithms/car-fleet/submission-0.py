class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # rearrage the two list with position, in ascending order

        data = zip(position, speed)
        s_data = sorted(data, key=lambda data: data[0], reverse=True)

        # calculate the time-needed to arrive

        t_needed = [((target-data_pt[0])/data_pt[1]) for data_pt in s_data] 

        # if the later is bigger than the previous one, the number of fleet +1

        fleets = 0
        last = []
        for i, t in enumerate(t_needed):
            while not last or last[1] < t:
                fleets += 1
                last = [i, t]
        return fleets