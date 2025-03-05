class Solution(object):
    def wordPattern(self, pat, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        f=1
        str=s.split()
        if(len(pat)!=len(str)):
            return False
        for i in range(0,len(pat)-1):
            for j in range(i+1,len(pat)):
                if((pat[i]==pat[j] and str[i]!=str[j]) or (pat[i]!=pat[j] and str[i]==str[j])):
                    f=0
                    return False
                else:
                    f=1
        for i in range(0,len(pat)-1):
            res=[]
            if(pat[i]!='!'):
                res.append(i)
                for j in range(i+1,len(pat)):
                    if(pat[i]==pat[j]):
                        res.append(j)
                pat=pat.replace(pat[i],'!')
                for i in range(0,len(res)-1):
                    for j in range(i+1,len(res)):
                        if(str[res[i]]==str[res[j]]):
                            f=1
                        else:
                            f=0
            if(f==0):
                break
        if(f):
            return True
        return False
solution=Solution()     
