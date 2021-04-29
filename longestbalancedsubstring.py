n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0) #we inserted 0 beacuse we need to start from the index1
stack=[]
l=[]
positive=0
negative=0
stack.append(0)

for i in range(1,len(arr)):
         if(arr[i]>0):
             stack.append(i)
             positive+=1
             continue
         if(arr[stack[-1]]==-1*arr[i]):
             stack.pop()
             negative+=1
            
             
         else:
             stack.append(i)
         if(negative==positive):
             l.append(negative+positive)
             positive=negative=0
print(max(l))

