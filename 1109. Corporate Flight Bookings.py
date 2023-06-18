class Solution:
    def corpFlightBookings(self, bookings, n):
        difference_block = [0 for _ in range(n+1)]
        for booking in bookings:
            difference_block[booking[0]-1] += booking[2]
            difference_block[booking[1]] -= booking[2]
        total = 0
        for i in range(n):
            total += difference_block[i]
            difference_block[i] = total
        return difference_block[:n]
