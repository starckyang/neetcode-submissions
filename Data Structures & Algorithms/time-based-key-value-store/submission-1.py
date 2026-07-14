class TimeMap:

    def __init__(self):
        self.tm = {}
        self.tmk = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = {}
            self.tmk[key] = []
        self.tm[key][timestamp] = value
        self.tmk[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        timekey = self.tmk[key]
        l, r = 0, len(timekey)-1
        if timekey[l] > timestamp:
            return ""
        while l <= r:
            m = (l+r)//2
            mn = timekey[m]
            if mn == timestamp:
                return self.tm[key][mn]
            if mn < timestamp:
                l = m+1
            else:
                r = m-1
        if mn > timestamp:
            return self.tm[key][timekey[m-1]]
        else:
            return self.tm[key][mn]
