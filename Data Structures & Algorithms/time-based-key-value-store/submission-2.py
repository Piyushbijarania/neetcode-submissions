class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data.get(key, [])
        if not arr:
            return ""
        
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if arr[mid][0] <= timestamp:
                l = mid
            else:
                r = mid - 1
        if arr[l][0] <= timestamp:
            return arr[l][1]
        else:
            return ""
        
