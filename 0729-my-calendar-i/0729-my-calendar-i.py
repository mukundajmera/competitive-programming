class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        isBooked = True
        idx = 0
        while idx < len(self.calendar):
            if self.calendar[idx][0] < end and start < self.calendar[idx][1]:
                isBooked = False
                break
            elif self.calendar[idx][0] >= end:
                break
            idx += 1
        
        if isBooked:
            self.calendar.insert(idx, [start,end])

        return isBooked

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)