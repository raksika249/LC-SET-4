class Solution(object):
    def maximumWealth(self, accounts):
        sum1=0
        sum2=0
        for i in accounts:
            sum1=0
            for j in i:
                sum1+=j
                if(sum1>sum2):
                    sum2=sum1
        return sum2
                
