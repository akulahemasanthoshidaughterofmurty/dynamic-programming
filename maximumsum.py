n=int(input())
count=0
maxsum=0
elements=input().split()
l=[]
for i in elements:
    l.append(int(i))
high=max(l)    
if(int(high)<0):
    print(high,1)
else:
    for i in l:
        if(int(i)>=0):
            maxsum+=int(i)
            count+=1
    print(maxsum,count)
