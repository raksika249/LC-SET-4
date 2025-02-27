class Solution(object):
    def xorOperation(self, n, start):
        res=0
        i=1
        a=[start]
        while(i<n):
            a.append(start+2*i)
            i+=1
        for i in a:
            res=res^i
        return res
solution=Solution()
