class Solution(object):
    def checkPowersOfThree(self, n):
        while(n!=0):
            rem=n%3
            n//=3
            if rem==2:
                return False
        return True
