def signFunc(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1
class Solution(object):
    def arraySign(self, nums):
        prod=1
        for i in nums:
            prod*=i
        return signFunc(prod)
solution=Solution()
