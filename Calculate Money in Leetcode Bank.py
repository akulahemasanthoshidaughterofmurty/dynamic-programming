class Solution:
    def totalMoney(self, n: int) -> int:
        m=1
        count=0
        l=[]
        l.insert(0,0)
        total=0
        while(count!=n):
            if(count%7==0 and count!=0):
                total=0
                m=m+1
                total=m
                l.append(m)
                count+=1
            else:
                total+=1
                l.append(total)
                count+=1
                
        newl=l[:n+1]
        res=sum(newl)
        return res
        
