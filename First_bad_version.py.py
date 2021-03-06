"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#I have used Binary search algorithm to solve the given problem
class Solution:
    def firstBadVersion(self, n):
        l=0
        while(l <= n):
            mid = int(l + ((n-l)/2))
            print(mid, n, l)
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    n = mid
                else:
                    return mid
            else:
                l = mid+1

"""
#A more optimized version of the same

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i <= j:
            m = (i+j) // 2
            if isBadVersion(m):
                j = m-1
            else:
                i = m+1
        if isBadVersion(i):
            return i
        return i-1"""