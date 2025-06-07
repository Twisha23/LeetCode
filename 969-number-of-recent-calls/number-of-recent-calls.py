class RecentCounter:

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        cnt = 0
        for time in reversed(self.times):
            if t - time <= 3000:
                cnt += 1
            else:
                break
        return cnt