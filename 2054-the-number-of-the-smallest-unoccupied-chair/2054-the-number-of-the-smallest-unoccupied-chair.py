class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # times.sort(key=lambda time: time[0])
        target_friend = times[targetFriend]
        times.sort()

        n = len(times)
        chair_timer = [0] * n

        for time in times:
            for idx in range(n):
                if chair_timer[idx] <= time[0]:
                    chair_timer[idx] = time[1]
                    if time == target_friend:
                        return idx
                    break

        return 0