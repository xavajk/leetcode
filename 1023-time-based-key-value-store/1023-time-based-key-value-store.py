class TimeMap:

    def __init__(self):
        # dict with, key: list of timestamp value pairs
        # note: timestamps given for set will be strictly increasing
        self.dict = {}

    def _bin_search(self, key: str, time: int) -> str:
        # bsearch of nearest minimum timestamp available
        res, times = '', self.dict.get(key, [])
        l, r = 0, len(times) - 1
        while l <= r:
            m = (l + r) // 2
            if times[m][0] <= time:
                res = times[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # do binary search on timestamps to find rightmost index of 
        # which value to choose (first greater than timestamp if not present)
        return self._bin_search(key, timestamp)

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)