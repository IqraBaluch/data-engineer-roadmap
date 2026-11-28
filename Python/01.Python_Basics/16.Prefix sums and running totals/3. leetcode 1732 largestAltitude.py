# a = [3, -1, 2]

a =[1, 1, -5, 4]

""""
====== COMPLEXITY =====

Time = O(n) due to n numbers of iterations

Space = O(1) dut to consatnt return value we are not saving any list other thn the current_altitude and highest_altitude

"""
class Solution:
    def largestAltitude(self, gain):
        a = gain
        current_altitude = 0
        highest_altitude =  0
  
        for i in range(len(a)):
            current_altitude = current_altitude + a[i]
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude

        return highest_altitude
print(Solution().largestAltitude([-1,1,-1,1,-1]))

assert Solution().largestAltitude([1,2,3,-1]) == 6
assert Solution().largestAltitude([]) == 0
assert Solution().largestAltitude([-2,3-1]) == 0
assert Solution().largestAltitude([5,5,5,5]) == 20

