class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0] * n
        for booking in bookings:
            output[booking[1] - 1] += booking[2]
            if booking[0] > 1:
                output[booking[0] - 2] -= booking[2]
            
        for i in range(n - 2, -1, -1):
            output[i] += output[i+1]
        return output
            
    
