class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count=0
        for i in arr:
            if(i%2==1):
                count+=1
            else:
                count=0
            if(count==3):
                return True
        return False
        
