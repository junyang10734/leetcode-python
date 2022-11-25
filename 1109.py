# 1109 Corporate Flight Bookings
# Array / 差分数组


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0 for _ in range(n+1)]
        for first,last,seats in bookings:
            arr[first] += seats
            if last < n:
                arr[last+1] -= seats
        
        for i in range(1, n+1):
            arr[i] += arr[i-1]
        
        return arr[1:]