class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times = sorted([(arrival, leave, index) for index, (arrival, leave) in enumerate(times)])

        next_chair = 0
        available_chairs = []
        leaving_queue = []

        for time in times:
            arrival, leave, index = time

            # Free up chairs based on current time
            while leaving_queue and leaving_queue[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_queue)
                heapq.heappush(available_chairs, chair)

            #utiilise from available chair first
            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                current_chair = next_chair
                next_chair += 1

            # Push current leave time and chair
            heapq.heappush(leaving_queue, (leave, current_chair))

            # Check if it's the target friend
            if index == targetFriend:
                return current_chair
        return 0

        # # times.sort(key=lambda time: time[0])
        # target_friend = times[targetFriend]
        # times.sort()

        # n = len(times)
        # chair_timer = [0] * n

        # for time in times:
        #     for idx in range(n):
        #         if chair_timer[idx] <= time[0]:
        #             chair_timer[idx] = time[1]
        #             if time == target_friend:
        #                 return idx
        #             break

        # return 0
