class Solution(object):
    def differenceOfSums(self, n, m):
        sum=0
        divSum=0
        for i in range(1,n+1):
            if(i%m!=0):
                sum+=i
            else:
                divSum+=i
        return sum-divSum 
solution=Solution()
