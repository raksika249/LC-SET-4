class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        prod=1
        while(n!=0):
            rem=n%10
            sum+=rem
            prod*=rem
            n/=10
        return prod-sum
